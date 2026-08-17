# 방법1 거버넌스 선례 — 표준화 기구 사례

조사일: 2026-08-17
대상: **공식 표준화 기구 6곳** — IETF · W3C · Ecma International · OASIS · OGC · ITU-T

> **기존 조사와 겹치지 않는다.** `표준문서-소스코드병행배포사례/`는 **무엇을 배포하는가**(스키마 파일·URL·라이선스)를 봤고, 이 조사는 **어떻게 운영하는가**(절차·역할·제도)를 본다. W3C·OGC처럼 기관이 겹치는 곳이 있으나, 앞선 조사는 `dcat.ttl`·`gml.xsd` 같은 **산출물**을 봤고 이 조사는 특허정책·URI 영속성 정책 같은 **제도 문서**를 본다.

## 왜 이 조사가 필요한가

방법1은 **공동 에디터를 두지 않고 제안 측이 스키마까지 책임지는** 구조다. 심의에서 나올 질문은 산출물이 아니라 절차에 관한 것이다.

- 전문가를 붙이지 않고 제안자에게 맡기는 선례가 있는가
- 참조구현 코드를 표준 밖에 두는 것이 타당한가
- 외부 저장소에 둔 것을 규범이라 할 수 있는가
- 제안 단계에 무언가를 선언하게 하는 제도가 있는가

이 조사는 그 답을 **표준화 기구의 실제 규정 문안**에서 찾는다.

## 조사 대상 기구

| 기구 | 원어 | 성격 |
|---|---|---|
| **IETF** | Internet Engineering Task Force | 인터넷 기술 표준화 기구 |
| **W3C** | World Wide Web Consortium | 웹 표준화 컨소시엄 |
| **Ecma** | Ecma International | 정보통신 국제 표준화 기구 (TC39가 ECMAScript 담당) |
| **OASIS** | Organization for the Advancement of Structured Information Standards | 구조화 정보 표준화 기구 |
| **OGC** | Open Geospatial Consortium | 개방형 지리공간 컨소시엄 |
| **ITU-T** | International Telecommunication Union – Telecommunication Standardization Sector | 국제전기통신연합 전기통신표준화부문 |

## 5개 축과 방법1 조문 대응

| 축 | 방법1 조문 | 핵심 질문 |
|---|---|---|
| [A. 에디터와 제안자 역할](#축-a-에디터와-제안자-역할) | 제19조의2 · 공동 에디터 **미설치** | 전문가 없이 제안 측이 끌고 가는 선례가 있나 |
| [B. 참조구현과 코드의 지위](#축-b-참조구현과-코드의-지위) | 제19조의3제6항 | 코드를 표준 밖에 두거나 별도 라이선스를 붙인 선례 |
| [C. 영속 보관과 이중 배포](#축-c-영속-보관과-이중-배포) | 제19조의3제4항 · 보관본이 정본 | 외부 배포와 기관 보관을 어떻게 잇나 |
| [D. 제출 검증 자동화](#축-d-제출-검증-자동화) | 제19조의3제7항 | 형식 점검을 절차에 넣은 선례 |
| [E. 제안 단계 선언 제도](#축-e-제안-단계-선언-제도) | 제13조제5항 · 선언서 | 제안 단계에 무엇을 선언하게 하나 |

---

## 축 A. 에디터와 제안자 역할

**방법1의 쟁점** — 어휘 전문가를 공동 에디터로 배정하지 않고, 제안자가 선언하고 에디터가 작성한다. "전문가 검증 없이 괜찮은가"라는 질문에 답해야 한다.

### Ecma TC39 — 챔피언(champion) 모델

가장 가까운 선례다. ECMAScript 제안은 **Stage 0~4**를 거치는데, 각 단계를 끌고 가는 주체가 **챔피언**이다.

수집한 프로세스 문서에서 확인되는 구조다.

> Stage 0 — "None. New proposals are assigned this stage by their authors outside of the usual advancement process."

**제안자(author)가 스스로 Stage 0에 올린다.** 위원회가 배정하는 것이 아니다. 이후 단계 진입 요건에 "챔피언 지정"이 포함되며, 챔피언이 명세 문안과 구현·테스트를 책임진다.

**방법1과의 관계** — 제안 측이 산출물을 책임지는 구조가 국제 표준화 기구에 이미 있다는 근거가 된다. TC39는 Ecma International의 정식 기술위원회이고, 그 결과물이 ECMA-262다.

| 파일 | 내용 |
|---|---|
| `Ecma-TC39_프로세스문서.html` | Stage 0~4 진입·종료 요건 |
| `Ecma-TC39_제안목록.md` | 실제 제안의 단계별 추적 현황 |

### IETF — 저자와 RFC 편집자의 분리

IETF는 문서 **저자(author)**와 **RFC 편집자(RFC Editor)**를 분리한다. 저자가 내용을 쓰고, RFC 편집자는 형식·문체를 담당한다. 내용에 대한 어휘 전문가를 별도로 배정하지 않는다.

| 파일 | 내용 |
|---|---|
| `IETF_RFC2026_인터넷표준절차.html` | 인터넷 표준화 절차 전반 (BCP 9) |
| `IETF_RFC7322_RFC스타일가이드.html` | RFC 편집자의 역할 범위 |

### W3C · OASIS · OGC · ITU-T — 에디터 제도

네 기구 모두 워킹그룹이 **에디터(Editor)**를 지정하고 에디터가 문안을 작성한다. 별도의 어휘 전문가 직위를 두는 기구는 확인되지 않았다.

| 파일 | 내용 |
|---|---|
| `W3C_프로세스문서.html` | 워킹그룹·에디터·문서 성숙 단계 |
| `OASIS_TC프로세스.html` | 기술위원회 구성과 에디터 |
| `OGC_정책개요.html` | 표준 작업반 운영 |
| `ITU-T_A1_권고안내.html` | 권고 A.1 (연구반 작업방법) 안내 — 본문은 세션 인증이 필요해 미수집 |

---

## 축 B. 참조구현과 코드의 지위

**방법1의 쟁점** — 참조구현을 표준의 일부에서 배제하고 부록에 위치만 안내한다. 근거가 필요하다.

### IETF Trust Legal Provisions 5.0 — **가장 직접적인 선례**

IETF는 **문서 안의 코드에 별도 라이선스를 적용**한다. 수집한 TLP 5.0 원문의 제4조다.

**4.a 정의**
> "IETF Contributions and IETF Documents often include components intended to be directly processed by a computer (**"Code Components"**)."

**4.b 식별 — 마커로 표시한다**
> "any text found between the markers **`<CODE BEGINS>` and `<CODE ENDS>`**, or otherwise clearly labeled as a Code Component, shall be considered a Code Component."

**4.c 라이선스 — 문서와 다른 조건**
> "such Code Components are also licensed ... on the terms of the **"Revised BSD License"** ... If a licensee elects to apply the BSD License to a Code Component, then the additional licenses and restrictions set forth in Section 3 **shall not apply thereto**."

**4.d 귀속**
> "Those who use Code Components ... are requested to attribute each such Code Component to IETF and identify the RFC ... from which it is taken."

**방법1과의 관계**

| IETF | 방법1 |
|---|---|
| 코드를 문서 **안에** 두되 마커로 구분하고 별도 라이선스 적용 | 코드를 문서 **밖에** 두고 부록에 위치만 안내 |
| 문서 제한이 코드에 미치지 않음을 명시 | 참조구현이 표준의 일부가 아님을 명시 |

**택한 방식은 다르지만 문제의식은 같다** — 문서와 코드는 성격이 달라 같은 규율을 적용할 수 없다는 것이다. 심의에서 "왜 코드를 배제하는가"라는 질문이 나오면, IETF도 코드를 문서와 분리해 다룬다는 점을 근거로 들 수 있다.

> **참고** — TLP 원문에 주석이 있다. 이전 판은 이 라이선스를 "Simplified BSD License"라 잘못 불렀고 IETF Trust가 2021년 9월 21일 "Revised BSD License"로 바로잡았다. 라이선스 본문은 처음부터 Revised BSD였다.

### W3C — 문서 라이선스와 소프트웨어 라이선스의 분리

W3C도 **문서용**과 **소프트웨어용** 라이선스를 나눠 둔다.

| 파일 | 내용 |
|---|---|
| `W3C_문서_라이선스.html` | 명세 문서에 적용 |
| `W3C_소프트웨어문서_라이선스.html` | 코드·테스트 스위트에 적용 |

`IETF_RFC8179_IPR공개.html`, `OASIS_IPR정책.html`도 함께 수집했다.

---

## 축 C. 영속 보관과 이중 배포

**방법1의 쟁점** — 스키마를 GitHub 등 외부에 두면서 협회 보관본을 정본으로 삼는다. 외부 배포와 기관 보관을 잇는 선례가 필요하다.

### W3C — URI 영속성 정책

W3C는 발간한 URI를 영구히 유지하겠다고 **명문으로 약속**한다. 수집한 정책 문서에 창립자의 선언이 인용돼 있다.

> "The intent is to set an example by **reducing the failure of links due to clumsy management or inadequate commitment to information persistence**, and to provide a stable reference base of information about W3C-related topics as a service to the community." — Tim Berners-Lee, 1999

**방법1과의 관계** — 방법1의 규범적 참조가 실효를 가지려면 참조 대상 URI가 유지되어야 한다. W3C는 이를 **기관 정책으로 문서화**했다. TTA가 네임스페이스 URI 체계를 도입할 때(3부 중장기 과제) 참고할 문안이다.

### W3C — 날짜 박힌 판과 최신판의 분리

W3C는 같은 문서를 두 주소로 낸다. `/TR/2024/REC-vocab-dcat-3-20240822/`(날짜 고정)와 `/TR/vocab-dcat-3/`(최신). **버전 고정과 최신 추적을 URI 수준에서 분리**한 방식이다.

방법1의 규범적 참조 명세가 "판 또는 버전"을 요구하는 것과 같은 취지다.

### Ecma — GitHub 개발 + 정식 발간의 이중 트랙

`Ecma_ECMA-424_발간페이지.html`에서 확인된다. CycloneDX 스키마는 GitHub에서 개발·배포되지만, 같은 버전이 **ECMA-424라는 정식 표준으로 발간**된다. 방법1의 "협회 보관본이 정본" 구조와 같은 형태다.

| 파일 | 내용 |
|---|---|
| `W3C_URI영속성_정책.html` | URI 영속성 약속 |
| `W3C_재발간_정책.html` | 재발간·이관 시 처리 |
| `IETF_RFC편집자_보존안내.html` | RFC 영구 보존 체계 |
| `Ecma_ECMA-424_발간페이지.html` | GitHub 개발분의 정식 발간 |
| `OGC_스키마저장소_정책.html` | `schemas.opengis.net` 운영 정책 |

---

## 축 D. 제출 검증 자동화

**방법1의 쟁점** — 사무국이 형식 정합성을 전자적 방법으로 점검할 수 있게 했다(제19조의3제7항). 재량 규정이라 근거가 약하다는 지적이 나올 수 있다.

### OGC — 적합성 시험 프로그램

OGC는 **CITE**(Compliance Interoperability Test and Evaluation)라는 적합성 시험 체계를 운영하고, **TEAM Engine**이라는 시험 엔진을 공개한다. 구현이 표준에 맞는지 기계적으로 검증하는 절차를 기구 차원에서 제도화했다.

**방법1과의 차이** — OGC는 **구현체**를 시험하고, 방법1 제19조의3제7항은 **산출물의 형식**을 점검한다. 범위가 다르지만, 표준화 기구가 자동 검증을 절차에 넣은 선례라는 점에서 참고가 된다.

### IETF — 저자 도구

IETF는 초안 제출 전 형식을 자동 점검하는 도구를 제공한다.

| 파일 | 내용 |
|---|---|
| `OGC_적합성시험_프로그램.html` | CITE 프로그램 개요 |
| `OGC_TEAM엔진.html` | 시험 엔진 |
| `IETF_저자도구_안내.html` | 초안 작성·검사 도구 |
| `W3C_검증기.html` | 마크업 검증 서비스 |

---

## 축 E. 제안 단계 선언 제도

**방법1의 쟁점** — 제안 단계에 별지 제11-1호로 어휘·산출물·이용조건을 선언하게 한다. "제안 단계에 그런 부담을 지우는 것이 맞나"라는 질문이 나올 수 있다.

### W3C 특허정책 — 배제(exclusion) 절차

W3C는 특정 시점에 발간된 문서를 **"특허 검토 및 배제를 위해 발간된"** 것으로 규정하고, 참가자가 그 기간에 배제 통지(Exclusion Notice)를 내지 않으면 무상 실시 의무를 진다.

> "a version of a W3C Specification ... that is **published for patent review and exclusion**"
> "As a condition of participating in a Working Group, each participant..."

**핵심은 시점이다.** 특정 단계에 선언하지 않으면 이후에는 주장할 수 없다. 방법1의 제안 단계 선언도 같은 구조다 — 나중에 다투지 않도록 **미리 밝히게 한다.**

### IETF RFC 8179 (BCP 79) — 기여 시점 공개 의무

IETF는 기여자가 아는 지식재산권을 **기여 시점에** 공개하도록 의무화한다.

### 기타

| 파일 | 내용 |
|---|---|
| `W3C_특허정책.html` | 배제 절차·RF 실시 의무 |
| `ITU-T_특허정책.html` | ITU-T/ISO/IEC 공통 특허정책 |
| `IEEE-SA_정책.html` | IEEE 표준협회 정책 |
| `Ecma_규정.html` | Ecma 규정(by-laws) |
| `IETF_RFC8179_IPR공개.html` | 기여 시점 공개 의무 |

---

## 수집 내역

| 축 | 파일 수 |
|---|---|
| A. 에디터와 제안자 역할 | 8 |
| B. 참조구현과 코드의 지위 | 6 |
| C. 영속 보관과 이중 배포 | 5 |
| D. 제출 검증 자동화 | 4 |
| E. 제안 단계 선언 제도 | 4 |

총 27개 문서 · 약 5.5MB

## 미수집 항목

| 대상 | 사유 |
|---|---|
| **ISO/IEC Directives Part 1·2** | `iso.org` 봇 차단(HTTP 403). 앞선 조사에서 ISO 19115-3 문서 페이지가 막힌 것과 같은 문제 |
| **ITU-T 권고 A.1 본문** | 세션 인증이 필요한 다운로드 경로. 안내 페이지만 수집 |

두 건 모두 필요하면 브라우저로 직접 내려받아 이 폴더에 넣으면 된다.

## 검증 기준

이 문서의 인용문은 모두 **수집한 파일에서 직접 추출**했다. 해석과 사실을 구분해 적었으며, 방법1과의 대응 관계 서술은 필자의 판단이다.
