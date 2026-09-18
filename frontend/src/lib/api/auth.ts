import { apiClient } from './client'
import type { GoogleLoginRequest, GoogleLoginData } from '@/lib/types'

export async function loginWithGoogle(payload: GoogleLoginRequest): Promise<GoogleLoginData> {
  return apiClient<GoogleLoginData>('/auth/google', {
    method: 'POST',
    body: JSON.stringify(payload),
  })
}
