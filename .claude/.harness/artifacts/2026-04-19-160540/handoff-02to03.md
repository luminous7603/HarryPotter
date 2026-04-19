# Handoff: Phase 2 → Phase 3

## 목표 (Goal)
해리포터 팬페이지 구축 (Astro 5 + Tailwind CSS v4)
성공 기준: 랜딩 페이지, 캐릭터 소개, 세계관 정보, 시리즈 소개, 향후 콘텐츠 섹션, 반응형

## 이번 페이즈가 파악한 것 (Findings)
- 관련 파일 목록: 없음 (새 프로젝트, .claude/ 디렉토리만 존재)
- 코드 컨벤션 핵심:
  - Tailwind v4: `@tailwindcss/vite` 플러그인, `global.css`에 `@import "tailwindcss"`
  - Content Collections: `src/content/config.ts`에 zod 스키마 정의
  - 동적 라우트: `[slug].astro` 패턴

## 다음 페이즈가 해야 할 것 (Next)
- Astro 5 프로젝트 초기화 계획 수립
- 페이지 구조 및 컴포넌트 계획
- Content Collections 스키마 설계 (characters, books, worldbuilding, upcoming)
- 디자인 테마 방향 결정 (해리포터 분위기)

## 참고 파일 (References)
- `.claude/.harness/artifacts/2026-04-19-160540/context.md`
- `.claude/.harness/context.md`
