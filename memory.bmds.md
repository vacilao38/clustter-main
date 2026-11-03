# Memória BMDS — clustter-main-431c2336ed

```bmds-json
{
  "bmds": "0.1",
  "kind": "manifest",
  "id": "bmds://clustter-main-431c2336ed/manifest/root",
  "rev": 1,
  "profile": "portable",
  "created_at": "2026-10-27T13:43:48-03:00",
  "slot_profile": [
    "núcleo",
    "fatos",
    "decisões",
    "pendências",
    "entidades",
    "cronologia",
    "evidências_e_conflitos",
    "chaves_de_recuperação"
  ]
}
```

```bmds-json
{
  "bmds": "0.1",
  "kind": "cache",
  "id": "bmds://clustter-main-431c2336ed/cell/pesquisa-de-negocio-propostas-nao-aceitas-b03078569d",
  "rev": 1,
  "cell_type": "atomic",
  "created_at": "2026-10-27T13:59:21-03:00",
  "tags": [
    "concorrentes",
    "estrategia",
    "negocio"
  ],
  "slots": [
    "Plano exploratório de negócio Clustter produzido em 27/10/2026; prioridades e preços são propostas não aceitas.",
    [
      "Pesquisa abrange Folk, Pile, Chain, Lake, Noon, Bridge e Thermo; legados fora da família foram excluídos.",
      "Busca em página oficial identificou outro negócio Clustter em clustter.tech; situação registral não examinada.",
      "Vídeo s3ITx5AxrAs representado pelo resumo fornecido pelo usuário, sem transcrição integral.",
      "Serviço ai-memory local recusou conexão; não houve consulta ou publicação bem-sucedida de wiki."
    ],
    [],
    [
      "Validar segmento e dor com clientes antes de definir produto comercial.",
      "Propostas para revisão do usuário: Folk como primeira hipótese, Pile como alternativa, piloto de implantação R$149 e rotina de 6h semanais.",
      "Investigar disponibilidade de marca; demanda, preço, retenção e custos ainda não medidos.",
      "Prévia HTML é local e restrita à sessão; registro persistente no Agendador do Windows falhou por acesso negado."
    ],
    [
      "Clustter",
      "Folk",
      "Pile",
      "Chain",
      "Lake",
      "Noon",
      "Bridge",
      "Thermo"
    ],
    [
      {
        "date": "2026-10-27",
        "event": "Plano baseado em documentação local, resumo do vídeo pelo usuário e 19 referências públicas; nenhum app ou campanha publicado."
      }
    ],
    {
      "sources": [
        "docs/PLANO-NEGOCIO-2026-10-27.md",
        "projects.json",
        "PENDENCIAS.md",
        "READMEs dos sete apps",
        "Resumo do vídeo fornecido pelo usuário"
      ],
      "uncertainty": [
        "Sem vendas ou retenção observadas.",
        "Concorrentes comparados por recursos declarados, sem benchmark.",
        "Propostas não equivalem a decisões aceitas."
      ],
      "conflicts": []
    },
    [
      "negocio",
      "estrategia",
      "concorrentes",
      "validacao",
      "folk",
      "pile",
      "marca",
      "90-dias"
    ]
  ],
  "provenance": {
    "operation": "write",
    "sources": [],
    "actor": "human"
  }
}
```
```bmds-json
{
  "bmds": "0.1",
  "kind": "stack",
  "id": "bmds://clustter-main-431c2336ed/stack/negocio",
  "rev": 1,
  "updated_at": "2026-10-27T13:59:21-03:00",
  "logical_clock": 1,
  "members": [
    {
      "id": "bmds://clustter-main-431c2336ed/cell/pesquisa-de-negocio-propostas-nao-aceitas-b03078569d",
      "rev": 1
    }
  ],
  "policy": {
    "soft_cells": 16,
    "hard_tokens": 4096,
    "keep_hot": 4
  }
}
```

```bmds-json
{
  "bmds": "0.1",
  "kind": "cache",
  "id": "bmds://clustter-main-431c2336ed/cell/memoria-ce86604449",
  "rev": 1,
  "cell_type": "atomic",
  "created_at": "2026-11-03T10:34:38-03:00",
  "tags": [],
  "slots": [
    "Avaliação exploratória de Steam/TUNIC no Tab S10 Lite de 6 GB; plano de teste local produzido, sem implementação aprovada nem desempenho medido.",
    [
      "Usuário confirmou 6 GB de RAM e declarou possuir licenças reais dos jogos.",
      "Samsung informa Exynos 1380/Mali-G68; TUNIC declara 8 GB e GTX 660/RX 460 como mínimo de PC, o que não é consumo medido.",
      "GameNative oferece a categoria de download/execução local, mas seus avisos incluem componentes proprietários; não presumir fork integral redistribuível.",
      "ai-memory indisponível nas ferramentas desta sessão; memória local sem indexação wiki."
    ],
    [],
    [
      "Proposta não aceita: testar runtime existente no tablet, cliente Steam original e TUNIC a 540p/720p, meta de 30 FPS sustentados antes de decidir MVP.",
      "Coletar modelo exato, Android/One UI/driver, acesso ao tablet e preferência sobre streaming.",
      "Revisar termos específicos e licenças dos componentes antes de distribuição; não afirmar conformidade integral apenas pela posse do jogo."
    ],
    [
      "TUNIC",
      "Steam",
      "Galaxy Tab S10 Lite",
      "Winlator",
      "GameNative",
      "Mali-G68"
    ],
    [
      {
        "date": "2026-11-03",
        "event": "Pesquisa e plano, sem instalar APK, baixar jogo, autenticar conta ou medir FPS."
      }
    ],
    {
      "sources": [
        "docs/PLANO-STEAM-ANDROID-TUNIC-2026-11-03.md",
        "Confirmação do usuário: 6 GB",
        "https://store.steampowered.com/app/553420/TUNIC/",
        "https://store.steampowered.com/subscriber_agreement/",
        "https://github.com/utkarshdalal/GameNative/blob/master/THIRD_PARTY_NOTICES"
      ],
      "uncertainty": [
        "Sem teste no aparelho",
        "Execução local é premissa de planejamento; streaming não confirmado",
        "Metas e arquitetura são propostas, não decisões aceitas",
        "Sem parecer jurídico individual"
      ]
    },
    [
      "steam",
      "android",
      "tunic",
      "tab-s10-lite",
      "emulacao",
      "mali",
      "plano"
    ]
  ],
  "provenance": {
    "operation": "write",
    "sources": [],
    "actor": "human"
  }
}
```
```bmds-json
{
  "bmds": "0.1",
  "kind": "stack",
  "id": "bmds://clustter-main-431c2336ed/stack/steam-android",
  "rev": 1,
  "updated_at": "2026-11-03T10:34:38-03:00",
  "logical_clock": 1,
  "members": [
    {
      "id": "bmds://clustter-main-431c2336ed/cell/memoria-ce86604449",
      "rev": 1
    }
  ],
  "policy": {
    "soft_cells": 16,
    "hard_tokens": 4096,
    "keep_hot": 4
  }
}
```
