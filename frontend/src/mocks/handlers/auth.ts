import { http, HttpResponse } from 'msw'
import type { GoogleLoginRequest, GoogleLoginResponse } from '@/lib/types'
import { decodeGoogleIdToken } from '../decodeGoogleIdToken'
import { upsertUser } from '../state'

const API_BASE = '/api'

export const authHandlers = [
  http.post(`${API_BASE}/auth/google`, async ({ request }) => {
    const body = (await request.json()) as GoogleLoginRequest
    const { sub: google_id, email, name } = decodeGoogleIdToken(body.id_token)
    const isNewUser = upsertUser(google_id, email, name)

    const response: GoogleLoginResponse = {
      success: true,
      data: {
        is_new_user: isNewUser,
        token: google_id,
        ...(isNewUser ? { next_step: 'questionnaire' as const } : {}),
      },
    }
    return HttpResponse.json(response, { status: 200 })
  }),
]
