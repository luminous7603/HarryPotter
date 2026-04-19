# 해리 포터 팬페이지

> **이 프로젝트는 [`harness` 스킬](/.claude/skills/harness/SKILL.md)의 POC(Proof of Concept)로 제작되었습니다.**  
> harness 스킬이 요구사항 분석 → 계획 → 코드 생성 → 테스트 → 문서화까지 8개 페이즈를 얼마나 자율적으로, 완전하게 수행할 수 있는지를 검증한 세션입니다.

---

## harness 스킬 POC 결과

### harness 스킬이란?

`harness`는 Claude Code 내 7~8단계 워크플로우를 자율 실행하는 프로젝트 내 커스텀 스킬입니다.

```
Phase 1: Clarify        — 요구사항 명확화 및 성공 기준 정의
Phase 2: Context Gather — 코드베이스/환경 탐색 (서브에이전트 위임)
Phase 3: Plan           — 태스크 분해, Wave 설계, 복잡도 검토 [승인 게이트]
Phase 4: Generate       — 코드 생성 (Wave 순차/병렬 실행) [승인 게이트]
Phase 5: Test           — 빌드 검증, Playwright UI 스모크 테스트
Phase 6: Evaluate       — 성공 기준별 PASS/FAIL 판정
Phase 7: Document       — 문서 업데이트, git 커밋
Phase 8: Retrospect     — 패턴 분석, memory.md 업데이트 (선택)
```

### 이번 POC 핵심 수치

| 항목 | 결과 |
|------|------|
| 총 소요 페이즈 | 8개 (Retrospect 포함) |
| 사용자 개입 횟수 | 6회 (방향 선택 3회 + 승인 2회 + Playwright 설치) |
| 생성된 파일 수 | 83개 (소스 41개, 콘텐츠 25개, 설정/아티팩트 17개) |
| 빌드 시 오류 수정 | 1건 (`Astro.site` 조건부 처리) |
| UI 스모크 테스트 | 18개 경로 전부 PASS |
| 성공 기준 달성 | 6/6 PASS |
| git 커밋 | `03313ef` — 83 files |

### 스킬 효율성 자가 평가

| 영역 | 평점 | 평가 |
|------|------|------|
| 요구사항 분석 완전성 | ★★★★☆ | 목적·기술·성공기준을 단계적으로 파악, 대안 2가지 근거 제시. `.gitignore` 등 인프라 요소 사전 식별 미흡 |
| 개발 효율성 | ★★★★★ | Wave 분리로 의존성 충돌 없이 30개+ 파일 순차 생성. TypeScript 오류 없이 첫 빌드 1건 수정으로 통과 |
| 테스트 완전성 | ★★★★☆ | Playwright 18경로 + 빌드 검증 + 타입체크. 모바일 뷰포트 실측 및 네비게이션 동작 테스트 미포함 |
| 아티팩트 추적성 | ★★★★★ | Phase별 handoff, plan, test, evaluate, generate.md로 전 과정 재현 가능 |
| **종합** | **★★★★☆ (4.3/5)** | 단순 프롬프트 대비 구조화된 페이즈 관리로 완성도·추적성 모두 향상 |

### 세션 전체 대화 로그

→ [SESSION_LOG.md](./SESSION_LOG.md) — 대화 전문 및 Claude의 세션 리뷰 포함

---

## 프로젝트 소개

Astro 5 + Tailwind CSS v4 기반 해리 포터 팬사이트. 마크다운 기반 Content Collections로 콘텐츠를 관리하며, 향후 새로운 해리포터 관련 콘텐츠를 손쉽게 추가할 수 있는 구조로 설계되었습니다.

## 기술 스택

| 기술 | 버전 | 역할 |
|------|------|------|
| [Astro](https://astro.build) | 5.x | 정적 사이트 프레임워크, Content Collections, 파일 기반 라우팅 |
| [Tailwind CSS](https://tailwindcss.com) | 4.x | 유틸리티 CSS (`@tailwindcss/vite` 플러그인 방식) |
| TypeScript | 5.x | 타입 안전성, Content Collections zod 스키마 |
| Playwright | 최신 | UI 스모크 테스트 (CI 선택적 적용) |

## 시작하기

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # dist/ 에 정적 파일 생성
npm run preview  # 빌드 결과 미리보기
```

## 페이지 구조

| 경로 | 내용 |
|------|------|
| `/` | 랜딩 페이지 (히어로, 기숙사, 캐릭터, 시리즈, 향후 콘텐츠) |
| `/characters` | 캐릭터 목록 및 상세 (해리, 헤르미온느, 론, 덤블도어, 볼드모트) |
| `/books` | 7권 시리즈 목록 및 각 권 상세 |
| `/world` | 세계관 (4대 기숙사, 호그와트, 마법 주문) |
| `/upcoming` | 향후 공개 예정 콘텐츠 |

## 콘텐츠 추가 방법

콘텐츠는 `src/content/` 아래 마크다운 파일로 관리됩니다.

### 캐릭터 추가 (`src/content/characters/`)

```markdown
---
name: 캐릭터 이름
house: Gryffindor  # Gryffindor | Slytherin | Ravenclaw | Hufflepuff | None
role: 역할
actor: 배우 이름 (선택)
order: 10          # 목록 정렬 순서
featured: false    # true면 랜딩 페이지에 노출
---

본문 내용
```

### 책 추가 (`src/content/books/`)

```markdown
---
title: 책 제목
number: 8
year: 2025
tagline: 한 줄 소개 (선택)
---

본문 내용
```

### 세계관 항목 추가 (`src/content/worldbuilding/`)

```markdown
---
title: 항목 제목
category: location  # house | spell | location | creature | object
order: 10
---

본문 내용
```

### 향후 콘텐츠 추가 (`src/content/upcoming/`)

```markdown
---
title: 콘텐츠 제목
type: 영화
releaseDate: 2025년 (선택)
teaser: 짧은 소개 문구
announced: true
---

상세 내용
```

## 프로젝트 구조

```
src/
  ├── pages/           # 라우팅 (index, characters, books, world, upcoming)
  ├── components/      # Header, Footer, Card, HouseCard, UpcomingBanner
  ├── layouts/         # BaseLayout, ContentLayout
  ├── content/         # Content Collections
  │   ├── characters/  # 캐릭터 마크다운
  │   ├── books/       # 책 마크다운
  │   ├── worldbuilding/ # 세계관 마크다운
  │   ├── upcoming/    # 향후 콘텐츠 마크다운
  │   └── config.ts    # zod 스키마 정의
  └── styles/          # global.css (Tailwind v4 테마 포함)
public/                # favicon.svg
```
