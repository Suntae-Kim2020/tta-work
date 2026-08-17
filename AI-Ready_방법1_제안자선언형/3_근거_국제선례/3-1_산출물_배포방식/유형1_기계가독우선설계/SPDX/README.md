# SPDX (SBOM, ISO/IEC 5962)

- **문서**: https://spdx.github.io/spdx-spec/v3.0.1/
- **코드**: https://spdx.org/schema/3.0.1/spdx-json-schema.json
- **방식**: 스펙 산문(Markdown)과 형식 모델(SHACL/OWL)이 같은 릴리스 파이프라인에 있고, JSON Schema는 SHACL 모델에서 자동 생성.

## 확보 내역

spdx-spec 저장소에 docs/(산문)·ontology/(spdx-model.ttl·jsonld)·schemas/(버전별 JSON Schema)가 한 저장소에 공존. ※ spdx.org/rdf/3.0.1/ 경로의 owl.ttl·shacl.ttl은 현재 404이며, 동일 산출물이 저장소 ontology/에 있음.

## 파일 목록 (총 90개)

- `문서_spdx-spec-v3.0.1.html`
- `코드_spdx-context.jsonld`
- `코드_spdx-json-schema-3.0.1.json`
- `코드_spdx-model.ttl`
- `코드_spdx-spec-repo/.editorconfig`
- `코드_spdx-spec-repo/.gitattributes`
- `코드_spdx-spec-repo/.github/dependabot.yml`
- `코드_spdx-spec-repo/.github/workflows/markdownlint.yml`
- `코드_spdx-spec-repo/.github/workflows/publish_common.yml`
- `코드_spdx-spec-repo/.github/workflows/publish_v3.yml`
- `코드_spdx-spec-repo/.github/workflows/validate_examples.yml`
- `코드_spdx-spec-repo/.github/workflows/validate_pull_request.yml`
- `코드_spdx-spec-repo/.gitignore`
- `코드_spdx-spec-repo/.markdownlint.json`
- `코드_spdx-spec-repo/CHANGELOG.md`
- `코드_spdx-spec-repo/CONTRIBUTING.md`
- `코드_spdx-spec-repo/LICENSE`
- `코드_spdx-spec-repo/bin/check-examples.sh`
- `코드_spdx-spec-repo/bin/make-mkdocs-config.sh`
- `코드_spdx-spec-repo/bin/pull-license-list.py`
- `코드_spdx-spec-repo/build.md`
- `코드_spdx-spec-repo/docs/annexes/class-hierarchy.md`
- `코드_spdx-spec-repo/docs/annexes/license-matching-guidelines-and-templates.md`
- `코드_spdx-spec-repo/docs/annexes/rdf-model.md`
- `코드_spdx-spec-repo/docs/annexes/spdx-license-expressions.md`
- `… 외 65개`
