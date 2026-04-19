---
phase: plan
status: approved
timestamp: 2026-04-19T16:20:00+09:00
next: generate
---

# Plan

## 태스크 목록

### [순차] Task 1: Astro 5 프로젝트 스캐폴딩
- 생성 파일: `package.json`, `astro.config.mjs`, `tsconfig.json`, `src/env.d.ts`
- 설명: Astro 5 + Tailwind v4 기본 설정 파일 생성

### [순차] Task 2: Tailwind v4 설정
- 생성 파일: `src/styles/global.css`
- 수정 파일: `astro.config.mjs`
- 설명: `@tailwindcss/vite` 플러그인 통합, 해리포터 테마 커스텀 CSS 변수 설정

### [병렬] Task 3: Content Collections 스키마
- 생성 파일: `src/content/config.ts`
- 설명: characters, books, worldbuilding, upcoming 컬렉션 zod 스키마 정의

### [병렬] Task 4: 샘플 콘텐츠 데이터
- 생성 파일: `src/content/characters/*.md` (해리, 헤르미온느, 론, 덤블도어, 볼드모트)
- 생성 파일: `src/content/books/*.md` (7권)
- 생성 파일: `src/content/worldbuilding/*.md` (4개 기숙사, 마법 주문, 호그와트)
- 생성 파일: `src/content/upcoming/*.md` (차후 공개 콘텐츠 1개 예시)
- 설명: 각 컬렉션의 마크다운 샘플 콘텐츠

### [순차] Task 5: 기본 레이아웃
- 생성 파일: `src/layouts/BaseLayout.astro`, `src/layouts/ContentLayout.astro`
- 설명: HTML 기반 레이아웃, SEO 메타태그, 글로벌 스타일 연결

### [병렬] Task 6: 공통 컴포넌트
- 생성 파일: `src/components/Header.astro`, `src/components/Footer.astro`, `src/components/Card.astro`, `src/components/HouseCard.astro`, `src/components/UpcomingBanner.astro`
- 설명: 네비게이션, 푸터, 카드 컴포넌트

### [병렬] Task 7: 랜딩 페이지
- 생성 파일: `src/pages/index.astro`
- 설명: 히어로 섹션, 기숙사 소개, 최신 콘텐츠, 향후 콘텐츠 예고

### [병렬] Task 8: 캐릭터 페이지
- 생성 파일: `src/pages/characters/index.astro`, `src/pages/characters/[slug].astro`
- 설명: 캐릭터 목록 + 상세 페이지 (Content Collections 기반 동적 라우트)

### [병렬] Task 9: 세계관 페이지
- 생성 파일: `src/pages/world/index.astro`, `src/pages/world/[slug].astro`
- 설명: 호그와트, 기숙사, 마법 주문 등 세계관 정보

### [병렬] Task 10: 시리즈/책 페이지
- 생성 파일: `src/pages/books/index.astro`, `src/pages/books/[slug].astro`
- 설명: 7권 시리즈 목록 + 각 권 상세

### [병렬] Task 11: 향후 콘텐츠 페이지
- 생성 파일: `src/pages/upcoming.astro`
- 설명: 차후 공개 예정 콘텐츠 소개 페이지

### [순차] Task 12: public 자산
- 생성 파일: `public/favicon.svg`
- 설명: 해리포터 테마 파비콘

## 실행 순서
1. Task 1 → Task 2 (순차 — 프로젝트 초기화)
2. Task 3 + Task 4 (병렬 — 콘텐츠 스키마 및 데이터)
3. Task 5 (순차 — 레이아웃)
4. Task 6 (병렬 — 공통 컴포넌트)
5. Task 7 + Task 8 + Task 9 + Task 10 + Task 11 (병렬 — 페이지)
6. Task 12 (순차 — 자산)

## 범위 검토
- 기존 코드 재사용 가능 부분: 없음 (새 프로젝트)
- 이번에 하지 않는 것: 서버사이드 API, 검색 기능, 사용자 인증, 댓글 시스템
- 복잡도: ⚠️ 신규 파일 약 30개 — 새 프로젝트 특성상 정상 범위, Wave 분리로 관리

## 실패 시나리오
| 태스크 | 실패 경로 | 대응 |
|---|---|---|
| Task 1 | npm 미설치 또는 버전 불일치 | Node.js 18+ 필요, package.json 수동 작성 후 진행 |
| Task 3 | Content Collections 스키마 타입 오류 | zod 스키마 재검토, optional 필드 처리 |
| Task 8-10 | getCollection() 반환 타입 오류 | config.ts 스키마와 데이터 파일 frontmatter 일치 확인 |
