========================================
PCCX 문서
========================================

PCCX (Parallel Compute Core eXecutor)는 Altifigence가 시작하고 운영하는
오픈소스 반도체 프로젝트입니다. 공개 RTL·검증 환경·기술 문서를 함께
발전시킵니다. SystemVerilog 개발자는 :doc:`docs/quickstart`\ 에서 시작하세요.

프로젝트
--------

.. grid:: 1 1 2 2
   :gutter: 3 4 4 4
   :class-container: pccx-ecosystem-grid

   .. grid-item-card:: :octicon:`cpu;1.2em;sd-mr-1` v002 RTL
      :link: https://github.com/pccxai/pccx-v002
      :link-type: url

      v002 RTL, 테스트벤치, Sail ISA 모델을 살펴보세요.

   .. grid-item-card:: :octicon:`cpu;1.2em;sd-mr-1` KV260 통합
      :link: https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260
      :link-type: url

      v002 코어를 사용하는 KV260 보드 통합, 런타임, 보드 테스트입니다.

   .. grid-item-card:: :octicon:`book;1.2em;sd-mr-1` 문서 소스
      :link: https://github.com/pccxai/pccx
      :link-type: url

      이 사이트의 영어·한국어 문서와 기여 안내입니다.

   .. grid-item-card:: :octicon:`beaker;1.2em;sd-mr-1` v003 RTL
      :link: https://github.com/pccxai/pccx-v003
      :link-type: url

      v003 아키텍처를 위한 RTL 설계와 테스트벤치입니다.

참여와 검증
------------

.. grid:: 1 1 2 2
   :gutter: 3 4 4 4
   :class-container: pccx-toolchain-grid

   .. grid-item-card:: :octicon:`terminal;1.2em;sd-mr-1` 기여 시작
      :link: docs/onboarding/getting-started
      :link-type: doc

      저장소 선택부터 RTL 살펴보기, 첫 기여 준비까지 안내합니다.

   .. grid-item-card:: :octicon:`project-roadmap;1.2em;sd-mr-1` 공개 참여 로드맵
      :link: docs/roadmap
      :link-type: doc

      테스트 환경 정비와 첫 기여 이슈, 기여 가이드의 개발 계획입니다.

   .. grid-item-card:: :octicon:`verified;1.2em;sd-mr-1` 검증 자료
      :link: docs/Evidence/index
      :link-type: doc

      시뮬레이션과 보드 테스트의 결과, 소스 버전, 로그를 확인하세요.

   .. grid-item-card:: :octicon:`terminal;1.2em;sd-mr-1` Digital Design Studio
      :link: https://docs.altifigence.com/ide/
      :link-type: url

      디지털 설계를 위한 Altifigence의 개발 도구를 소개합니다.

.. toctree::
   :maxdepth: 2
   :caption: 소개

   docs/index
   docs/quickstart
   docs/onboarding/getting-started
   docs/Evidence/index
   docs/roadmap

.. toctree::
   :maxdepth: 1
   :caption: v002 아키텍처

   docs/v002/index

.. toctree::
   :maxdepth: 1
   :caption: 타겟 하드웨어

   docs/Devices/index

.. toctree::
   :maxdepth: 1
   :caption: 아카이브

   docs/archive/index

.. toctree::
   :maxdepth: 1
   :caption: 외부 링크

   Digital Design Studio <https://docs.altifigence.com/ide/>
   Altifigence.com <https://altifigence.com/>
   PCCX Transparency <https://pccx.ai/ko-kr/legal/transparency/>
