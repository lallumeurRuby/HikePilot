'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { submitQuestionnaireAnswers, ApiClientError } from '@/lib/api'
import { mockQuestionnaireQuestions } from '@/mocks/fixtures'
import { Toast } from '@/components/Toast'

export default function QuestionnairePage() {
  const router = useRouter()
  const [answers, setAnswers] = useState<Record<string, string>>({})
  const [submitting, setSubmitting] = useState(false)
  const [toast, setToast] = useState<string | null>(null)

  function updateAnswer(code: string, value: string) {
    setAnswers((prev) => ({ ...prev, [code]: value }))
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    setSubmitting(true)
    try {
      const payload = {
        answers: Object.entries(answers)
          .filter(([, value]) => value.trim() !== '')
          .map(([question_code, answer_value]) => ({
            question_code: question_code as (typeof mockQuestionnaireQuestions)[number]['code'],
            answer_value,
          })),
      }
      await submitQuestionnaireAnswers(payload)
      setToast('問卷已送出')
      router.push('/recommendations')
    } catch (err) {
      setToast(err instanceof ApiClientError ? err.message || err.violationType : '送出失敗，請重試')
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <div style={{ maxWidth: 600 }}>
      <h1>個人條件問卷</h1>
      <p>必答題以 * 標示；選填題可略過。</p>
      <form onSubmit={handleSubmit} data-testid="questionnaire-form">
        {mockQuestionnaireQuestions.map((q) => (
          <div key={q.code} style={{ marginBottom: '0.75rem' }}>
            <label htmlFor={`answer-${q.code}`}>
              {q.code}. {q.question_text}
              {q.is_required && <span aria-hidden="true"> *</span>}
            </label>
            <input
              id={`answer-${q.code}`}
              data-testid={`answer-${q.code}`}
              value={answers[q.code] ?? ''}
              onChange={(e) => updateAnswer(q.code, e.target.value)}
              required={q.is_required}
              style={{ display: 'block', width: '100%' }}
            />
          </div>
        ))}
        <button data-testid="questionnaire-submit" type="submit" disabled={submitting}>
          {submitting ? '送出中…' : '送出問卷'}
        </button>
      </form>
      {toast && <Toast message={toast} onClose={() => setToast(null)} />}
    </div>
  )
}
