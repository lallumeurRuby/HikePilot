'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { submitQuestionnaireAnswers, ApiClientError } from '@/lib/api'
import { mockQuestionnaireQuestions } from '@/mocks/fixtures'
import type { QuestionnaireQuestion } from '@/lib/types'
import { Toast } from '@/components/Toast'

function parseMultiChoice(value: string | undefined): string[] {
  return (value ?? '').split(',').map((v) => v.trim()).filter(Boolean)
}

function parseMatrix(value: string | undefined): Record<string, string> {
  const result: Record<string, string> = {}
  for (const pair of (value ?? '').split(',')) {
    const [scenarioCode, optionCode] = pair.split(':')
    if (scenarioCode && optionCode) result[scenarioCode.trim()] = optionCode.trim()
  }
  return result
}

function serializeMatrix(matrix: Record<string, string>): string {
  return Object.entries(matrix)
    .map(([scenarioCode, optionCode]) => `${scenarioCode}:${optionCode}`)
    .join(',')
}

function QuestionField({
  question,
  value,
  onChange,
}: {
  question: QuestionnaireQuestion
  value: string
  onChange: (value: string) => void
}) {
  const { code, answer_type, options, scenarios, is_required } = question

  if (answer_type === 'open_text') {
    return (
      <input
        id={`answer-${code}`}
        data-testid={`answer-${code}`}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        required={is_required}
        style={{ display: 'block', width: '100%' }}
      />
    )
  }

  if (answer_type === 'single_choice') {
    return (
      <div data-testid={`answer-${code}`} role="radiogroup">
        {options?.map((opt) => (
          <label key={opt.code} style={{ display: 'block' }}>
            <input
              type="radio"
              name={`answer-${code}`}
              data-testid={`answer-${code}-${opt.code}`}
              checked={value === opt.code}
              onChange={() => onChange(opt.code)}
              required={is_required}
            />
            {opt.text}
          </label>
        ))}
      </div>
    )
  }

  if (answer_type === 'multi_choice') {
    const selected = parseMultiChoice(value)
    return (
      <div data-testid={`answer-${code}`}>
        {options?.map((opt) => (
          <label key={opt.code} style={{ display: 'block' }}>
            <input
              type="checkbox"
              data-testid={`answer-${code}-${opt.code}`}
              checked={selected.includes(opt.code)}
              onChange={(e) => {
                const next = e.target.checked
                  ? [...selected, opt.code]
                  : selected.filter((c) => c !== opt.code)
                onChange(next.join(','))
              }}
            />
            {opt.text}
          </label>
        ))}
      </div>
    )
  }

  if (answer_type === 'matrix_single_choice') {
    const matrix = parseMatrix(value)
    return (
      <table data-testid={`answer-${code}`} style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th></th>
            {options?.map((opt) => (
              <th key={opt.code} style={{ fontWeight: 'normal', fontSize: '0.85em' }}>
                {opt.text}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {scenarios?.map((scenario) => (
            <tr key={scenario.code}>
              <td>{scenario.text}</td>
              {options?.map((opt) => (
                <td key={opt.code} style={{ textAlign: 'center' }}>
                  <input
                    type="radio"
                    name={`answer-${code}-${scenario.code}`}
                    data-testid={`answer-${code}-${scenario.code}-${opt.code}`}
                    checked={matrix[scenario.code] === opt.code}
                    onChange={() => onChange(serializeMatrix({ ...matrix, [scenario.code]: opt.code }))}
                    required={is_required}
                  />
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    )
  }

  return null
}

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
            <QuestionField
              question={q}
              value={answers[q.code] ?? ''}
              onChange={(value) => updateAnswer(q.code, value)}
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
