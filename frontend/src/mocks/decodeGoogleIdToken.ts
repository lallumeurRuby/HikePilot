export interface DecodedGoogleIdToken {
  sub: string
  email: string
  name: string
}

// Mock-only helper: decodes (does NOT verify) a Google ID token's payload.
// Real signature/issuer/audience verification happens on the real backend
// (backend/app/core/google_oauth.py) — this mock stands in for that backend only.
export function decodeGoogleIdToken(idToken: string): DecodedGoogleIdToken {
  const payloadSegment = idToken.split('.')[1]
  const base64 = payloadSegment.replace(/-/g, '+').replace(/_/g, '/')
  const json =
    typeof atob === 'function' ? atob(base64) : Buffer.from(base64, 'base64').toString('utf-8')
  const payload = JSON.parse(json)
  return { sub: payload.sub, email: payload.email, name: payload.name ?? '' }
}
