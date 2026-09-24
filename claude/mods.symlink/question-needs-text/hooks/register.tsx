import type { Register } from 'claude-code'

// Text the owner must read before a question has to reach them whole.
// On Claude Opus 5.5 the API turns text written between tool calls into a
// progress-update thinking block, and the owner sees only a one-line summary.
// The model's own text survives only at the start or end of a turn, so the mod
// gives it a tool, show_to_user, whose input is drawn in full, and refuses a
// question asked with neither visible text nor that tool in the same response.

const PLUGIN = 'question-needs-text'
const SHOW = 'show_to_user'
const SHOW_FULL = `mcp__${PLUGIN}__${SHOW}`

const REASON =
  `${PLUGIN}: this response has no visible text before the question. Text ` +
  'written between tool calls reaches the owner only as a summary. Put the ' +
  `item text, analysis and proposal into ${SHOW_FULL}, then ask again.`

// Whether the owner got something to read since the last answered question.
// Set by visible text or show_to_user; cleared when a turn starts and when a
// question is answered, so a retry after a failed call needs no second showing.
let shownSinceAnswer = false

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.tool.register({
      name: SHOW,
      description:
        'Show the owner a message verbatim, drawn in full as markdown. Use it ' +
        'for text the owner must read in the middle of a turn, such as the ' +
        'analysis before an AskUserQuestion call: text written between tool ' +
        'calls otherwise reaches the owner only as a one-line summary.',
      inputSchema: {
        type: 'object',
        properties: {
          text: { type: 'string', description: 'The message, in markdown.' },
        },
        required: ['text'],
      },
      isDeferred: false,
    })
    return next(e)
  })

  on('turn.start', ($, e, next) => {
    if (e.agentId === undefined) {
      shownSinceAnswer = false
    }
    return next(e)
  })

  on('turn.step', async function* ($, e, next) {
    if (e.agentId !== undefined) {
      return yield* next(e)
    }
    const stream = next(e)
    for await (const chunk of stream) {
      if (chunk.kind === 'text' && chunk.text.trim() !== '') {
        shownSinceAnswer = true
      }
      yield chunk
    }
    return await stream.result
  })

  on('tool.call', { tool: /^mcp__question-needs-text__show_to_user$/ }, ($, e, next) => {
    if (e.agentId === undefined) {
      shownSinceAnswer = true
    }
    return { result: 'Shown to the owner in full.' }
  }).catch(() => ({ result: 'Shown to the owner in full.' }))

  on('tool.call', { tool: 'AskUserQuestion' }, async ($, e, next) => {
    if (e.agentId !== undefined) {
      return next(e)
    }
    if (!shownSinceAnswer) {
      return { deny: REASON }
    }
    const answered = await next(e)
    if (answered.deny === undefined && answered.isError !== true) {
      shownSinceAnswer = false
    }
    return answered
  }).catch(($, e, next) => next(e))

  on('ui.render', { component: 'ToolUse' }, ($, e, next) => {
    const input = e.props.input as { text?: unknown } | undefined
    if (e.props.tool !== SHOW_FULL || typeof input?.text !== 'string') {
      return next(e)
    }
    const { Box, Markdown } = $.ui.resolve(e)
    return (
      <Box marginY={1}>
        <Markdown text={input.text} />
      </Box>
    )
  })
}
