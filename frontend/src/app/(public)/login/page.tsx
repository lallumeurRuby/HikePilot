'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { GoogleOAuthProvider, GoogleLogin, CredentialResponse } from '@react-oauth/google'
import { loginWithGoogle, ApiClientError } from '@/lib/api'
import { Toast } from '@/components/Toast'

// Google OAuth 流程本身不在本系統可測試邊界內（見 auth/使用者透過Google登入.feature 前置規則）
export default function LoginPage() {
  const router = useRouter()
  const [error, setError] = useState<string | null>(null)

  async function handleSuccess(credentialResponse: CredentialResponse) {
    setError(null)
    const idToken = credentialResponse.credential
    if (!idToken) {
      setError('登入失敗，請重試')
      return
    }
    try {
      const data = await loginWithGoogle({ id_token: idToken })
      document.cookie = `auth-token=${data.token}; path=/`
      // Activity Diagram: S1 -> S2 一律導向問卷頁（可選擇是否更新既有答案）
      router.push('/questionnaire')
    } catch (err) {
      setError(err instanceof ApiClientError ? err.message : '登入失敗，請重試')
    }
  }

  return (
    <main style={{ maxWidth: 400, margin: '4rem auto', padding: '1rem' }}>
      <h1>HikePilot 登山路線推薦</h1>
      <p>使用 Google 帳號登入/註冊</p>
      <GoogleOAuthProvider clientId={process.env.NEXT_PUBLIC_GOOGLE_CLIENT_ID!}>
        <GoogleLogin onSuccess={handleSuccess} onError={() => setError('登入失敗，請重試')} />
      </GoogleOAuthProvider>
      {error && <Toast message={error} onClose={() => setError(null)} />}
    </main>
  )
}
