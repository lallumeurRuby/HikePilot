import { http, HttpResponse } from 'msw'
import type { SubmitQuestionnaireRequest, SuccessResponse, ErrorResponse } from '@/lib/types'
import { extractGoogleIdFromAuthHeader, getUser, setAnswers } from '../state'

const API_BASE = '/api'
const REQUIRED_CODES = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q11']

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

    setAnswers(googleId, answerMap)
    const response: SuccessResponse = { success: true }
    return HttpResponse.json(response, { status: 200 })
  }),
]
