import { http, HttpResponse } from 'msw'
import type { SubmitQuestionnaireRequest, SuccessResponse, ErrorResponse } from '@/lib/types'
import { extractGoogleIdFromAuthHeader, getUser, setAnswers } from '../state'
import { mockQuestionnaireQuestions } from '../fixtures'

const API_BASE = '/api'
const REQUIRED_CODES = ['Q1', 'Q2', 'Q2B', 'Q3', 'Q4', 'Q5', 'Q11']

function isValidAnswerValue(questionCode: string, value: string): boolean {
  const question = mockQuestionnaireQuestions.find((q) => q.code === questionCode)
  if (!question || question.answer_type === 'open_text') return true

  const validOptionCodes = new Set((question.options ?? []).map((o) => o.code))

  if (question.answer_type === 'matrix_single_choice') {
    const validScenarioCodes = new Set((question.scenarios ?? []).map((s) => s.code))
    return value.split(',').every((pair) => {
      const [scenarioCode, optionCode] = pair.split(':')
      return !!scenarioCode && !!optionCode
        && validScenarioCodes.has(scenarioCode.trim())
        && validOptionCodes.has(optionCode.trim())
    })
  }

  const codes = value.split(',').map((v) => v.trim()).filter(Boolean)
  return codes.length > 0 && codes.every((c) => validOptionCodes.has(c))
}

export const profileHandlers = [
  http.post(`${API_BASE}/profile/questionnaire`, async ({ request }) => {
    const googleId = extractGoogleIdFromAuthHeader(request.headers.get('authorization'))
    if (!googleId || !getUser(googleId)) {
      const error: ErrorResponse = { success: false, error: { violation_type: 'UNAUTHENTICATED' } }
      return HttpResponse.json(error, { status: 401 })
    }

    const body = (await request.json()) as SubmitQuestionnaireRequest
    const answerMap = Object.fromEntries(
      body.answers.map((a) => [a.question_code, a.answer_value])
    )
    const missing = REQUIRED_CODES.filter((code) => !answerMap[code])
    if (missing.length > 0) {
      const error: ErrorResponse = {
        success: false,
        error: { violation_type: 'MISSING_REQUIRED_ANSWER', message: `缺少必答題：${missing.join(', ')}` },
      }
      return HttpResponse.json(error, { status: 400 })
    }

    const invalid = body.answers.find((a) => !isValidAnswerValue(a.question_code, a.answer_value))
    if (invalid) {
      const error: ErrorResponse = {
        success: false,
        error: { violation_type: 'INVALID_OPTION_CODE', message: `不合法的選項代碼：${invalid.question_code}` },
      }
      return HttpResponse.json(error, { status: 400 })
    }

    setAnswers(googleId, answerMap)
    const response: SuccessResponse = { success: true }
    return HttpResponse.json(response, { status: 200 })
  }),
]
