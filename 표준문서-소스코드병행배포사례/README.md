# 표준 문서·소스코드 병행 배포 사례

원본: `표준 문서·소스코드 병행 배포 사례.pdf` (상위 폴더)
수집일: 2026-08-14

국제·국가 표준화 기관이 **표준 문서(산문)와 기계가독 산출물(스키마·온톨로지)을 어떻게 함께 배포하는가**를
6개 유형 16개 사례로 나누어 실물 자산을 수집한 것이다. 각 사례 폴더의 `README.md`에 출처 URL·배포 방식·확보 내역이 있다.

파일명 규칙: `문서_*` = 표준 문서(산문), `코드_*` = 기계가독 규범 산출물, `메타_*` = 릴리스 메타데이터.

## 유형 1. 기계가독 우선 설계 — 스키마가 규범, 문서는 그로부터 생성

| 사례 | 확보한 핵심 자산 |
|---|---|
| NIST OSCAL | v1.2.3 릴리스 자산 52종(모델별 XSD·JSON Schema·변환 XSLT) |
| HL7 FHIR | R5 definitions(JSON·XML), XSD 323개, JSON Schema·ShEx·GraphQL·RDF |
| SPDX | 3.0.1 JSON Schema + spdx-spec 저장소(docs·ontology·schemas 동거) |
| CycloneDX | ECMA-424 2판 PDF(566쪽, 무료) + 버전별 XSD·JSON Schema·Protobuf |

## 유형 2. 공용 구조화 DB (NIST CPRT)

| 사례 | 확보한 핵심 자산 |
|---|---|
| NIST AI RMF 1.0 | AI 100-1 PDF + CPRT JSON·XLSX·graph, CSF 2.0 대조본, CPRT 전체 메타데이터 |

산문은 PDF로, 구조화 콘텐츠는 CPRT에 별도 등재하는 방식. AI RMF와 CSF 2.0을 함께 받아 대조한 결과
두 프레임워크가 `documents·elements·relationship_types·relationships` 라는 **동일 스키마**를 쓴다는 점을 확인했다.

## 유형 3. 네임스페이스 URI 역참조 (W3C·DCMI)

| 사례 | 확보한 핵심 자산 |
|---|---|
| W3C DCAT 3 | 권고안 HTML + dcat.ttl·rdf·jsonld |
| W3C PROV-O | 권고안 HTML + prov.owl·prov.ttl |
| Dublin Core | DCMI Terms HTML + dublin_core_terms.ttl |

## 유형 4. GitHub 저장소 단일 소스

| 사례 | 확보한 핵심 자산 |
|---|---|
| Schema.org | latest 덤프 6종(JSON-LD·TTL·RDF·N-Triples·CSV) + 저장소(schema.ttl 규범 소스) |
| MLCommons Croissant | 스펙 HTML v1.0 + croissant.ttl + 저장소 전체(스펙 md와 어휘 ttl 동거) |

## 유형 5. 문서 유료 + 스키마 무료 (ISO)

| 사례 | 확보한 핵심 자산 |
|---|---|
| ISO 19115-3 | 19115AllNamespaces.zip(공식 일괄 배포본, XSD 117개) + mdb 2.0 진입점 |

문서 본문은 iso.org 유료 판매(수집 불가)이나 규범 XSD는 standards.iso.org에서 무료 공개된다.
**ISO 체계 안에서도 스키마 무료 공개가 성립함**을 보여주는 사례.

## 유형 6. 같은 디렉터리 병행 게시 (도서관·지리·사회과학 메타데이터)

| 사례 | 확보한 핵심 자산 |
|---|---|
| LoC PREMIS | Data Dictionary PDF + premis.xsd |
| LoC MODS | 안내 HTML + mods-3-8.xsd |
| LoC METS | 안내 HTML + mets.xsd |
| OGC | 표준 목록 + GML 3.2.1 전체 모듈 XSD 29개 |
| DDI-Lifecycle 3.3 | 스펙 HTML + instance.xsd |

## 활용 포인트

- **스펙트럼 논거**: 유형 1(OSCAL·FHIR)은 스키마가 규범이고 문서가 파생물이며, 유형 5(ISO)조차 스키마는 무료 공개한다.
  AI-Ready Standard·Code-as-Standard 논거에 직접 사용 가능.
- **메타데이터 표준으로 한정**하면 DCAT·Dublin Core·Croissant·ISO 19115-3·PREMIS·MODS·DDI가 해당.

## 수집 시 확인된 원본 PDF와의 차이

| 항목 | 원본 PDF 기재 | 실제 |
|---|---|---|
| OSCAL v1.2.3 자산 수 | 54개 | 52개 |
| FHIR ShEx 파일명 | `definitions.shex.zip` | `fhir.schema.shex.zip` (원 파일명은 404) |
| SPDX SHACL/OWL 위치 | `spdx.org` 게시 | 해당 경로 404, 동일 산출물이 저장소 `ontology/`에 존재 |
| OGC GML | `gml.xsd` 단일 파일 | include 진입점이라 모듈 29개 전체를 함께 수집 |
| ISO 19115-3 XSD | 약 28개 모듈 | 모듈 28개 기준이나 일괄 배포본에는 관련 표준 포함 XSD 117개 |

## 수집 파일의 버전 관리

수집한 실물 파일(약 274MB)은 **git에 커밋하지 않는다.** OSCAL·FHIR·ISO·Schema.org 등 외부 기관의 배포본이라 이 과제의 산출물이 아니고, 커밋하면 저장소가 5.7MB에서 280MB로 커진다. RG/TG 원 표준 PDF에 적용한 방침과 같다(`.gitignore` 참조).

**커밋 대상은 분석 문서뿐이다** — 이 README, 사례별 README 16종, `저작권-라이선스-분석.md`, `스키마유형-제공방법-분석.md`.

실물 파일은 OneDrive에 그대로 있다. 다른 환경에서 다시 받으려면 각 사례 폴더 README의 **문서·코드 URL**을 따른다. 각 README에 출처 URL과 확보 내역이 파일 단위로 적혀 있다.

## 미수집 항목

- **ISO 19115-3 문서 본문** — iso.org 유료 판매 + Cloudflare 봇 차단. 유형 5의 정의상 예상된 결과.
