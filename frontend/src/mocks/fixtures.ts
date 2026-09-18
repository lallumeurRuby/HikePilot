// Fixtures traceable to specs/features/**/*.feature Given/Background 具體值
import type { QuestionnaireQuestion, RouteSummary, PlanSection } from '@/lib/types'

function opts(pairs: [string, string][]): { code: string; text: string }[] {
  return pairs.map(([code, text]) => ({ code, text }))
}

// specs/features/profile/填寫個人條件問卷.feature Background
export const mockQuestionnaireQuestions: QuestionnaireQuestion[] = [
  {
    code: 'Q1',
    question_text: '最近一年登山頻率',
    answer_type: 'single_choice',
    is_required: true,
    options: opts([
      ['Q1-1', '幾乎沒有登山經驗'],
      ['Q1-2', '每半年約1-2次'],
      ['Q1-3', '每2-3個月約1次'],
      ['Q1-4', '約每月1-2次'],
      ['Q1-5', '約每週或每兩週1次'],
      ['Q1-6', '每週多次'],
    ]),
  },
  {
    code: 'Q2',
    question_text: '曾完成且最接近能力上限的路線（路線名稱）',
    answer_type: 'open_text',
    is_required: true,
  },
  {
    code: 'Q2B',
    question_text: '上述路線完成時的體感',
    answer_type: 'single_choice',
    is_required: true,
    options: opts([
      ['Q2B-1', '非常輕鬆'],
      ['Q2B-2', '輕鬆'],
      ['Q2B-3', '適中'],
      ['Q2B-4', '有挑戰但可完成'],
      ['Q2B-5', '非常吃力／接近極限'],
      ['Q2B-6', '中途放棄或需要協助'],
    ]),
  },
  {
    code: 'Q3',
    question_text: '一般天氣路況下可舒適完成的單日行程',
    answer_type: 'single_choice',
    is_required: true,
    options: opts([
      ['Q3-1', '2小時以內'],
      ['Q3-2', '2-4小時'],
      ['Q3-3', '4-6小時'],
      ['Q3-4', '6-8小時'],
      ['Q3-5', '8-10小時'],
      ['Q3-6', '10小時以上'],
    ]),
  },
  {
    code: 'Q4',
    question_text: '已具備或能獨立操作的登山經驗類型',
    answer_type: 'multi_choice',
    is_required: true,
    options: opts([
      ['Q4-1', '一般步道健行'],
      ['Q4-2', '陡坡／連續階梯'],
      ['Q4-3', '原始山徑'],
      ['Q4-4', '碎石／岩石地形'],
      ['Q4-5', '拉繩／需手腳並用地形'],
      ['Q4-6', '夜間行走'],
      ['Q4-7', '地圖／離線地圖判讀'],
      ['Q4-8', 'GPX導航'],
      ['Q4-9', '渡溪'],
      ['Q4-10', '高山過夜／山屋'],
      ['Q4-11', '露營／背負裝備'],
      ['Q4-12', '高海拔3000m以上'],
      ['Q4-13', '雪季／冰雪地形'],
      ['Q4-14', '無上述經驗'],
    ]),
  },
  {
    code: 'Q5',
    question_text: '對各類登山情境的風險接受程度',
    answer_type: 'matrix_single_choice',
    is_required: true,
    scenarios: opts([
      ['steepness', '陡峭上坡／下坡'],
      ['scrambling', '手腳並用攀爬'],
      ['exposure', '暴露感強的稜線／高落差地形'],
      ['altitude', '高海拔環境'],
      ['navigation_difficulty', '路徑不明顯／需要自行導航'],
    ]),
    options: opts([
      ['Q5-1', '不接受'],
      ['Q5-2', '盡量避免'],
      ['Q5-3', '視情況可接受'],
      ['Q5-4', '可以接受'],
      ['Q5-5', '喜歡／主動選擇'],
    ]),
  },
  {
    code: 'Q6',
    question_text: '偏好的行程節奏',
    answer_type: 'single_choice',
    is_required: false,
    options: opts([
      ['Q6-1', '悠閒，經常休息拍照'],
      ['Q6-2', '偏悠閒'],
      ['Q6-3', '適中'],
      ['Q6-4', '偏快，以完成路線為主'],
      ['Q6-5', '挑戰型，偏好高強度'],
    ]),
  },
  {
    code: 'Q7',
    question_text: '偏好的行程時間',
    answer_type: 'single_choice',
    is_required: false,
    options: opts([
      ['Q7-1', '2小時以內'],
      ['Q7-2', '2-4小時'],
      ['Q7-3', '4-6小時'],
      ['Q7-4', '6-8小時'],
      ['Q7-5', '8-10小時'],
      ['Q7-6', '不限定'],
    ]),
  },
  {
    code: 'Q8',
    question_text: '偏好的人潮狀況',
    answer_type: 'single_choice',
    is_required: false,
    options: opts([
      ['Q8-1', '熱門、人多也可以'],
      ['Q8-2', '有一些人比較安心'],
      ['Q8-3', '無特別偏好'],
      ['Q8-4', '偏好人少'],
      ['Q8-5', '越安靜、越少人越好'],
    ]),
  },
  {
    code: 'Q9',
    question_text: '希望登山行程包含的體驗',
    answer_type: 'multi_choice',
    is_required: false,
    options: opts([
      ['Q9-1', '山頂展望'],
      ['Q9-2', '日出'],
      ['Q9-3', '日落'],
      ['Q9-4', '森林'],
      ['Q9-5', '瀑布／溪流'],
      ['Q9-6', '湖泊'],
      ['Q9-7', '雲海'],
      ['Q9-8', '季節花卉／植物'],
      ['Q9-9', '野生動物／生態'],
      ['Q9-10', '歷史／人文遺跡'],
      ['Q9-11', '攝影'],
      ['Q9-12', '高山景觀'],
      ['Q9-13', '稜線行走'],
      ['Q9-14', '攀爬／刺激地形'],
      ['Q9-15', '溫泉'],
      ['Q9-16', '山屋／住宿體驗'],
      ['Q9-17', '露營'],
      ['Q9-18', '百岳／小百岳／山岳蒐集'],
    ]),
  },
  {
    code: 'Q10',
    question_text: '理想中的登山行程描述',
    answer_type: 'open_text',
    is_required: false,
  },
  {
    code: 'Q11',
    question_text: '需特別考量的身體狀況或需求',
    answer_type: 'multi_choice',
    is_required: true,
    options: opts([
      ['Q11-1', '無特殊需求'],
      ['Q11-2', '膝蓋容易不適'],
      ['Q11-3', '腳踝／足部容易不適'],
      ['Q11-4', '腰背容易不適'],
      ['Q11-5', '心肺耐力較弱'],
      ['Q11-6', '容易喘／需要較頻繁休息'],
      ['Q11-7', '懼高'],
      ['Q11-8', '容易暈眩'],
      ['Q11-9', '不適合長時間曝曬'],
      ['Q11-10', '不適合低溫環境'],
      ['Q11-11', '不適合高海拔'],
      ['Q11-12', '需要較頻繁補水／休息'],
      ['Q11-13', '其他'],
    ]),
  },
]

// specs/features/auth/使用者透過Google登入.feature Examples
export const mockUsers = {
  alice: { google_id: 'g-001', email: 'alice@example.com', name: 'Alice' },
  bob: { google_id: 'g-002', email: 'bob@example.com', name: 'Bob' },
}

// specs/features/profile/填寫個人條件問卷.feature「必答題全部填寫、選填題略過時操作成功」Example
export const mockAliceAnswers: Record<string, string> = {
  Q1: 'Q1-6',
  Q2: '郊山一日健行',
  Q2B: 'Q2B-2',
  Q3: 'Q3-4',
  Q4: 'Q4-7,Q4-9',
  Q5: 'steepness:Q5-4,scrambling:Q5-1,exposure:Q5-2,altitude:Q5-3,navigation_difficulty:Q5-3',
  Q11: 'Q11-1',
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
