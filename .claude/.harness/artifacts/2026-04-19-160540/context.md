---
phase: context-gather
status: approved
timestamp: 2026-04-19T16:15:00+09:00
next: plan
---

# Context

## 프로젝트 구조 요약

Astro 5 표준 디렉토리 구조:

```
src/
  ├── pages/              (라우팅 대상 파일들)
  ├── components/         (재사용 가능한 UI 컴포넌트)
  ├── layouts/            (페이지 레이아웃 템플릿)
  ├── content/            (Content Collections - 콘텐츠 저장소)
  │   ├── characters/     (캐릭터 소개 콘텐츠)
  │   ├── books/          (시리즈/책 소개 콘텐츠)
  │   ├── worldbuilding/  (세계관 정보 콘텐츠)
  │   └── config.ts       (Content Collections 설정)
  ├── styles/             (CSS/Tailwind 스타일)
  ├── assets/             (이미지, 폰트 등 정적 자산)
  ├── utils/              (유틸리티 함수)
  └── types/              (TypeScript 타입 정의)
public/                    (처리하지 않은 정적 자산)
astro.config.mjs          (Astro + Tailwind 설정)
```

## 코드 컨벤션

- **Content Collections**: `src/content/config.ts`에서 스키마 정의, 하위 디렉토리별 `.md`/`.mdx` 파일 저장
- **Tailwind v4**: `@tailwindcss/vite` 플러그인 사용, `src/styles/global.css`에서 `@import "tailwindcss"` 선언
- **라우팅**: `src/pages/` 파일 이름 = URL 경로, 동적 라우트는 `[slug].astro` 패턴

## 관련 기존 파일

없음 (새 프로젝트) — 프로젝트 루트에는 `.claude/` 디렉토리만 존재

## 참고 사항

1. **Content Collections API**: 모든 컬렉션은 `src/content/` 내 최상위 폴더여야 함
2. **Astro 5.2+**: `npx astro add tailwind` 명령으로 자동 설정 가능
3. **동적 라우트**: 캐릭터/책 상세 페이지는 `[slug].astro` 패턴 사용
4. **TypeScript**: `src/content/config.ts`에서 `defineCollection()` + `z` 스키마로 타입 명시
