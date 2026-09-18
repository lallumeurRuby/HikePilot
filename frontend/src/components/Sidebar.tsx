'use client'

const navItems = [
  { href: '/questionnaire', label: '個人條件問卷' },
  { href: '/recommendations', label: '路線推薦' },
]

export function Sidebar() {
  return (
    <aside data-testid="sidebar" style={{ width: 240, borderRight: '1px solid #eee', padding: '1rem' }}>
      <nav data-testid="sidebar-nav">
        {navItems.map((item) => (
          <a key={item.href} href={item.href} style={{ display: 'block', marginBottom: '0.5rem' }}>
            {item.label}
          </a>
        ))}
      </nav>
    </aside>
  )
}
