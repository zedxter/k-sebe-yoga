---
version: alpha
name: K-Sebe-Yoga
description: Тёплый, изысканный и тихий — премиальная студийная эстетика для йоги в парке. Воздух, лёгкость, крупная элегантная типографика, сдержанная тёплая палитра.
colors:
  primary: "#3D2F28"
  secondary: "#8A7A6E"
  tertiary: "#C98153"
  neutral: "#FFF8EF"
  on-primary: "#FFF8EF"
  on-tertiary: "#FFFFFF"
  surface: "#F7EDE1"
typography:
  h1:
    fontFamily: Cormorant Garamond
    fontSize: 2.8rem
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: "-0.01em"
  h2:
    fontFamily: Cormorant Garamond
    fontSize: 1.7rem
    fontWeight: 500
    lineHeight: 1.2
  lead:
    fontFamily: Cormorant Garamond
    fontSize: 1.6rem
    fontWeight: 400
    lineHeight: 1.5
  body-md:
    fontFamily: Inter
    fontSize: 1.02rem
    fontWeight: 400
    lineHeight: 1.75
  body-small:
    fontFamily: Inter
    fontSize: 0.92rem
    fontWeight: 400
    lineHeight: 1.6
  button:
    fontFamily: Inter
    fontSize: 0.98rem
    fontWeight: 500
    lineHeight: 1.4
  manifesto-item:
    fontFamily: Cormorant Garamond
    fontSize: 1.25rem
    fontWeight: 400
    lineHeight: 1.6
  closing:
    fontFamily: Cormorant Garamond
    fontSize: 1.5rem
    fontWeight: 400
    lineHeight: 1.4
  meta:
    fontFamily: Inter
    fontSize: 0.85rem
    fontWeight: 400
    lineHeight: 1.9
  label-small:
    fontFamily: Inter
    fontSize: 0.8rem
    fontWeight: 500
    lineHeight: 1.4
rounded:
  sm: 4px
  md: 8px
  lg: 14px
  xl: 16px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
components:
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.on-tertiary}"
    rounded: "{rounded.full}"
    padding: 14px 26px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.xl}"
    padding: 24px
  card-notes:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.xl}"
    padding: 32px
  manifesto:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: 0
    padding: 24px
  check-marker:
    backgroundColor: "{colors.tertiary}"
    size: 8px
    rounded: "{rounded.full}"
---

## Overview

K-Sebe-Yoga — одностраничный лендинг для бесплатной уличной йоги в парке Ruinenberg (Потсдам). Аудитория: русскоязычные женщины 25–50 лет в Берлине и Потсдаме.

Визуальный характер — **изысканный и тихий**. Не паф-панель. Воздух, лёгкость, крупная элегантная serif-типографика, сдержанная тёплая палитра. Ощущение премиальной мягкой студии, где не надо ничего доказывать. Никакого «фитнес-брендинга» — это пространство для возвращения к себе.

Бренд принадлежит Юлии (@Yulia_yoga_innere_balance), проект некоммерческий. Landing говорит от первого лица — мягко, приглашающе, без спама и агрессивных CTA.

## Colors

- **Primary (#3D2F28):** Тёплый шоколад — основной текст заголовков и тела. Никакого чистого чёрного (#000000).
- **Secondary (#8A7A6E):** Приглушённый — мета-данные, footer, подписи. Держит иерархию, не отвлекает.
- **Tertiary (#C98153):** Терракота — единственный акцент. Используется **только** для CTA-кнопок и заголовков-акцентов (в манифесто). Не размазывать.
- **Neutral (#FFF8EF):** Мраморно-бежевый фон страницы. Тёплый, воздушный, не кричит.
- **Surface (#F7EDE1):** Подложка карточек (card, manifesto, notes). Чуть глубже фона.
- **On-primary (#FFF8EF):** Текст на primary-фоне (не используется — primary это сам текст).
- **On-tertiary (#FFFFFF):** Белый текст поверх терракотовой CTA-кнопки.

> **Внимание, контраст:** комбинация tertiary (#C98153) + on-tertiary (#FFFFFF) даёт контраст ~3.1:1, что ниже WCAG AA (4.5:1) для обычного текста. Это сознательное решение для декоративного акцента (CTA-кнопка крупная, текст не мелкий). Для body-текста контраст primary на neutral > 8:1 — отлично.

## Typography

Два шрифта — serif для заголовков, sans для тела. Контраст между ними создаёт иерархию.

- **Cormorant Garamond** (Google Fonts): h1, h2, lead, manifesto-item, closing. Премиальный, «студийный». Курсив — в эмоциональных местах: manifesto-item, closing.
- **Inter** (Google Fonts): body, meta, button, label. Чистый гротеск, контраст с serif. Fallback: system-ui, -apple-system, Segoe UI, sans-serif.

Подгрузка: `<link>` из Google Fonts с кириллическим подмножеством (cyrillic — весь контент русский).

Иерархия: h1 → lead → h2 → body. Межстрочные просторные (line-height 1.6–1.8 для тела). Крупные h1 с воздухом вокруг; на мобильном адаптивный clamp (через CSS, не в токенах — clamp невалиден для DESIGN.md).

## Layout

Страница — одноширинный центр (max-width: 720px) с полноширинным hero-блоком сверху (edge-to-edge).

### Секции

1. **Hero** — полноширинная обложка (edge-to-edge, ~72vh на десктопе) + HTML-оверлей (h1 + lead + CTA + trust). Десктоп: горизонтальная картинка (hero-wide.jpg), фигура слева, текст в правой колонке ~58%. Мобильный: вертикальная full-height (hero-mobile.jpg), текст в верхней части, фигура по центру 35–80% вертикали. Скролл-нэйм (chevron ⌄) внизу. Градиентный оверлей для читаемости.
2. **Lead** — центрированная свободная строка.
3. **What this is** — текст + manifesto (карточка с левой акцентной полосой из CSS border-left).
4. **Why morning** — заголовок + абзац.
5. **What to bring** — check-список с круглыми маркерами.
6. **Contact / details** — notes-карточка (время, цена, локация, CTA).
7. **Closing** — финальная фраза курсивом.
8. **Footer** — подпись.

### Hero (критичный раздел)

- Обложка = один целостный кадр, не коллаж. Утверждённая база: cover.jpg (24.08).
- На картинке НЕТ текста — все надписи HTML/CSS-оверлеем.
- Женская фигура целиком, без обрезки сверху/снизу.
- Строчка доверия под CTA: «Практика в парке · 40–50 минут · бесплатно».
- Картинка чистая — без логотипов, водяных знаков, вшитых подписей.

### Сетка

Отступы: секции разделены xl (48px). Воздух — главный элемент премиального ощущения. Мобильная адаптивность проверяется на **320–414px** (docErr=0).

## Components

- **button-primary**: единственная высоко-эмфазная кнопка на странице. Pill-форма (rounded.full), терракотовый фон, белый текст. CSS дополнительно: тень rgba(201,129,83,.55), на hover translateY(-2px) + усиление тени.
- **card**: универсальная подложка. Тёплый бежевый (surface), rounded.xl. Без тени.
- **card-notes**: вариант карточки для секции контакта. Увеличенный padding. CSS дополнительно: рамка 1px solid rgba(201,129,83,.28).
- **manifesto**: карточка с левой акцентной полосой (4px твердой левой границы CSS border-left цвета tertiary). Элементы внутри — курсивный Cormorant Garamond (typography.manifesto-item).
- **check-marker**: кружок-маркер для списка «С собой». Цвет tertiary, размер 8px, скругление full. В CSS реализуется как `::before` псевдоэлемент.

## Do's and Don'ts

### Do

- **Do** использовать токен-ссылки (`{colors.tertiary}`) вместо сырых hex в компонентах.
- **Do** проверять мобильную адаптивность на 320–414px перед публикацией.
- **Do** хранить картинки без вшитого текста — весь текст рендерится HTML/CSS-оверлеем.
- **Do** использовать один акцентный цвет на страницу, не размазывать.
- **Do** расширять палитру только через этот DESIGN.md, не в CSS.
- **Do** использовать cover.jpg как единственный источник для hero-фото (утверждено 24.08).
- **Do** сохранять женскую фигуру целиком — без обрезки сверху или снизу.

### Don't

- **Don't** использовать чистый чёрный текст (#000000) — только `{colors.primary}` (#3D2F28).
- **Don't** вшивать текст в изображения — ни логотипы, ни надписи, ни водяные знаки.
- **Don't** генерировать коллаж из разных локаций — hero-фото = один целостный кадр (cover.jpg).
- **Don't** менять позу/ракурс/силуэт женщины из cover.jpg — она остаётся точь-в-точь.
- **Don't** использовать тень на карточках — тени только у интерактивных элементов (кнопки на hover).
- **Don't** добавлять цвета вне палитры — сначала расширить её в DESIGN.md.
- **Don't** использовать несколько акцентов на одной странице (RainbowStrip анти-паттерн).
- **Don't** выравнивать всё по центру (CenterCrutch) — hero-композиция асимметрична.

## Anti-patterns

### 1. Text-on-image overflow
Текст hero-секции на мобильном экране наезжает на фигуру женщины, перекрывая её.
- **Причина:** текст позиционирован без учёта вертикального расположения фигуры.
- **Фикс:** текст в верхней части (выше макушки), женщина по центру ~35–80% по вертикали.
- **Статус:** ✅ Исправлено (hero-copy absolute, top: .9rem на ≤720px).

### 2. Cut-off figure
Женская фигура обрезана сверху или снизу на мобильном из-за `object-fit: cover`.
- **Причина:** `object-fit: cover` обрезает контент под контейнер.
- **Фикс:** на мобильном position:relative + ширина 100% + высота auto (не обрезает); full-height вертикальная картинка с родным aspect ratio 9:16.
- **Статус:** ✅ Исправлено.

### 3. Collage hallucination
При генерации cover-изображения модель смешивает элементы разных локаций (неоклассические руины, средневековый замок, аллея из другого места).
- **Причина:** ИИ-генерация комбинирует элементы из разных источников.
- **Канон:** один целостный кадр (cover.jpg), утверждённый 24.08. Не смешивать локации, не добавлять фантазийные элементы.
- **Статус:** ✅ Канон установлен.

### 4. No trust signal under CTA
Отсутствие короткого факта надёжности под первой CTA-кнопкой снижает доверие и конверсию.
- **Причина:** кнопка без контекста висит в воздухе.
- **Фикс:** строчка доверия (trust line): «Практика в парке · 40–50 минут · бесплатно».
- **Статус:** ✅ Исправлено.

### 5. RainbowStrip (base)
Все цвета палитры одновременно — визуальный шум. В k-sebe-yoga: строго один акцентный цвет (tertiary), остальные — нейтральные/текстовые.

### 6. CenterCrutch (base)
Всё выровнено по центру — нет иерархии, трудно сканировать. В k-sebe-yoga: hero-текст прижат вправо (асимметричная композиция с фигурой слева). Секции ниже — центрированы осознанно (тихий тон).