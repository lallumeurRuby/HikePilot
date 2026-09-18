// Fixtures traceable to specs/features/**/*.feature Given/Background 具體值
import type { QuestionnaireQuestion, RouteSummary, PlanSection } from '@/lib/types'

// specs/features/profile/填寫個人條件問卷.feature Background
export const mockQuestionnaireQuestions: QuestionnaireQuestion[] = [
  { code: 'Q1', question_text: '最近一年登山頻率', answer_type: 'single_choice', is_required: true },
  { code: 'Q2', question_text: '曾完成且最接近能力上限的路線與完成時體感', answer_type: 'open_text', is_required: true },
  { code: 'Q3', question_text: '一般天氣路況下可舒適完成的單日行程', answer_type: 'single_choice', is_required: true },
  { code: 'Q4', question_text: '已具備或能獨立操作的登山經驗類型', answer_type: 'multi_choice', is_required: true },
  { code: 'Q5', question_text: '對各類登山情境的風險接受程度', answer_type: 'matrix_single_choice', is_required: true },
  { code: 'Q6', question_text: '偏好的行程節奏', answer_type: 'single_choice', is_required: false },
  { code: 'Q7', question_text: '偏好的行程時間', answer_type: 'single_choice', is_required: false },
  { code: 'Q8', question_text: '偏好的人潮狀況', answer_type: 'single_choice', is_required: false },
  { code: 'Q9', question_text: '希望登山行程包含的體驗', answer_type: 'multi_choice', is_required: false },
  { code: 'Q10', question_text: '理想中的登山行程描述', answer_type: 'open_text', is_required: false },
  { code: 'Q11', question_text: '需特別考量的身體狀況或需求', answer_type: 'multi_choice', is_required: true },
]

// specs/features/auth/使用者透過Google登入.feature Examples
export const mockUsers = {
  alice: { google_id: 'g-001', email: 'alice@example.com', name: 'Alice' },
  bob: { google_id: 'g-002', email: 'bob@example.com', name: 'Bob' },
}

// specs/features/profile/填寫個人條件問卷.feature「必答題全部填寫、選填題略過時操作成功」Example
export const mockAliceAnswers: Record<string, string> = {
  Q1: '幾乎每週都有登山',
  Q2: '已完成郊山一日健行，體感輕鬆',
  Q3: '6-8 小時',
  Q4: '地圖判讀, 溪谷渡溪',
  Q5: '陡峭石階:可接受, 需垂降地形:不接受',
  Q11: '無特殊身體狀況',
}

// specs/features/recommendation/請求路線推薦.feature「有符合條件路線時推薦 1~3 條」Example
export const mockRoutes: RouteSummary[] = [
  { route_id: 1, name: '路線一' },
  { route_id: 2, name: '路線二' },
]

// specs/features/plan/生成登山規劃書.feature「後置（回應）- 規劃書須包含以下區塊」Rule
export const mockPlanSections: PlanSection[] = [
  { section_order: 1, section_name: '路線摘要' },
  { section_order: 2, section_name: '分段行程' },
  { section_order: 3, section_name: '天氣路況' },
  { section_order: 4, section_name: '風險應對' },
  { section_order: 5, section_name: '裝備補給' },
  { section_order: 6, section_name: '交通資訊' },
  { section_order: 7, section_name: '緊急應變（撤退條件、替代方案）' },
  { section_order: 8, section_name: '行前 Checklist' },
]

export const mockPdfUrl = 'https://mock.hikepilot.example/plans/demo-plan.pdf'
