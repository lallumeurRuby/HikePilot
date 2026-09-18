// 模擬後端的記憶體狀態（僅供 MSW mock 使用，重新整理頁面即重置）
import type { RouteSummary } from '@/lib/types'

interface MockUserRecord {
  google_id: string
  email: string
  name: string
  answers: Record<string, string>
}

const users = new Map<string, MockUserRecord>()
const lastRecommendation = new Map<string, RouteSummary[]>()

export function getUser(googleId: string): MockUserRecord | undefined {
  return users.get(googleId)
}

export function upsertUser(google_id: string, email: string, name: string) {
  const isNew = !users.has(google_id)
  if (isNew) {
    users.set(google_id, { google_id, email, name, answers: {} })
  }
  return isNew
}

export function setAnswers(googleId: string, answers: Record<string, string>) {
  const user = users.get(googleId)
  if (!user) return
  user.answers = { ...user.answers, ...answers }
}

export function getRequiredAnswered(googleId: string): boolean {
  const user = users.get(googleId)
  if (!user) return false
  const required = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q11']
  return required.every((code) => !!user.answers[code])
}

export function setLastRecommendation(googleId: string, routes: RouteSummary[]) {
  lastRecommendation.set(googleId, routes)
}

export function getLastRecommendation(googleId: string): RouteSummary[] {
  return lastRecommendation.get(googleId) ?? []
}

export function extractGoogleIdFromAuthHeader(authHeader: string | null): string | null {
  if (!authHeader?.startsWith('Bearer ')) return null
  const token = authHeader.slice('Bearer '.length)
  return token || null
}
