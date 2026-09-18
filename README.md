<div align="center">

<img src="assets/banner.png" alt="openGym" width="720">

<br>

**Um rastreador de academia e peso corporal self-hosted que é realmente seu.**

Planeje sua semana, faça treinos guiados, registre cada série e seu peso corporal ao longo do tempo —
no celular, sincronizado entre dispositivos, com login por passkey.
Sem conta em servidor de terceiros, sem assinatura, sem anúncios. Só `docker compose up`.

<br>

[![License: AGPL v3](https://img.shields.io/badge/license-AGPL--3.0-a3e635?style=flat-square)](LICENSE)
![Self-hosted](https://img.shields.io/badge/self--hosted-%F0%9F%8F%A0-60a5fa?style=flat-square)
![PWA](https://img.shields.io/badge/PWA-instalável-a78bfa?style=flat-square)
![React](https://img.shields.io/badge/React-19-38bdf8?style=flat-square&logo=react&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-compose-2496ED?style=flat-square&logo=docker&logoColor=white)
![No tracking](https://img.shields.io/badge/telemetria-nenhuma-f472b6?style=flat-square)
<br>
![GitHub last commit](https://img.shields.io/github/last-commit/dougllassillva27/openGym?style=flat-square)
[![GitHub stars](https://img.shields.io/github/stars/dougllassillva27/openGym?style=flat-square)](https://github.com/dougllassillva27/openGym/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/dougllassillva27/openGym?style=flat-square)](https://github.com/dougllassillva27/openGym/issues)

</div>

<br>

> ### 🤖 Este é um fork — adiciona o Treinador IA
>
> Um fork do [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) que adiciona uma
> funcionalidade opcional: uma IA que **cria** seu plano de treino e **revisa com base no que você
> realmente registra**, rodando no seu próprio servidor com sua própria conta de provedor.
>
> Todo o resto é o openGym original. Com o Treinador desativado, o app é idêntico ao projeto de origem.
>
> **→ [O que faz e como usar](docs/AI_COACH.md)** ·
> [Configuração Claude](Claude-setup-instructions.md) ·
> [Configuração ChatGPT / Codex](ChatGPT-setup-instructions.md) ·
> [apresentação de design (PDF)](openGym_AI_Strategy.pdf)

<br>

<div align="center">
<table>
<tr>
<td align="center"><img src="assets/screenshots/home.png" alt="Início" width="230"><br><sub><b>Início</b> — treino e peso de hoje</sub></td>
<td align="center"><img src="assets/screenshots/workout.png" alt="Treino" width="230"><br><sub><b>Treino guiado</b> — demos animadas e séries</sub></td>
<td align="center"><img src="assets/screenshots/stats.png" alt="Estatísticas" width="230"><br><sub><b>Estatísticas</b> — heatmap, gráficos e recordes</sub></td>
</tr>
</table>
</div>

<div align="center">

### [🌐 opengym.duarte-santos.ch](https://opengym.duarte-santos.ch) · [▶ Teste a demo ao vivo](https://duartesantos8.github.io/openGym/)

Sem cadastro, nada para instalar — roda inteiramente no navegador com dados de exemplo.<br>
<sub>Não há servidor por trás da demo, então login por passkey, sincronização entre dispositivos e o
painel de administração só existem numa instância self-hosted.</sub>

</div>

## Por quê

A maioria dos apps de treino tranca seus dados num login em servidores deles, te enche de notificação para assinar, ou desaparece quando a startup fecha. O openGym é o oposto: **roda na sua máquina, seus dados ficam numa pasta que você controla, e o código é seu para fazer fork.** E ainda assim é moderno — instalável como app na tela inicial, login por passkey, suporte offline, sincronização entre celular e computador.

## Funcionalidades

- ⚖️ **Rastreamento de peso corporal** — gráfico interativo com linha de meta que você define; ganhos/perdas coloridos conforme se aproximam dela
- 🏋️ **Plano semanal** — uma rotina por dia da semana, com uma biblioteca de **1.324 exercícios** (pesquisáveis, com demos animadas)
- 🗓️ **Reagende qualquer dia** — ficou doente, perdeu um treino, ou menos dias na academia esta semana? Mova o treino para outro dia sem mexer no plano semanal
- ▶️ **Treinos guiados** — sabe que dia é hoje e começa a sessão do dia; pede seu peso primeiro, preenche os pesos da última vez, temporizador de descanso, detecção de recordes, rastreamento de peso por exercício
- ☀️ **A tela não apaga enquanto você treina** — sem precisar desbloquear o celular e procurar onde estava entre as séries. Ligada enquanto o treino roda, liberada assim que termina, e desativável nas Configurações
- 🔗 **Superséries** — monte e registre seguidas, descansando só depois do par
- ⏱️ **Exercícios cronometrados** — pranchas, barras fixas, agachamento isométrico e carregamentos são registrados por tempo, não reps, com um cronômetro de trabalho que conta a série (separado do descanso) e registra o tempo que você realmente sustentou. Também aceitam peso
- 📈 **Progressão com regra definida** — escolha uma por rotina, sobrescreva por exercício: linear, **Greyskull LP** (série AMRAP final, saltos duplos, resets de 10%), progressão dupla por intervalo de reps, ou adicionar tempo. Seus pesos já vêm corretos quando a sessão abre, e cada meta explica *por que* aquele número. Reps falhadas nunca avançam a carga, estagnações disparam deload, e exercícios com peso corporal progridem em reps
- 💪 **1RM estimado** — por exercício, a partir da melhor série elegível (ele diz qual), com curva de progresso própria e calculadora para séries que você não fez. Não estima acima de 12 reps
- 🎯 **Esforço por série, na sua escala** — uma terceira coluna opcional avaliando a dificuldade da série, como **RIR** (reps de reserva) ou **RPE** (o mesmo julgamento numa escala de 10). Desativado por padrão; cada série mantém a escala em que foi registrada, e mais nada lê o valor — progressão e 1RM não são afetados
- 🏃 **Cardio** — registre tempo + velocidade, não só peso × reps
- 📤 **Compartilhe um plano** — envie suas rotinas e agenda semanal como um arquivo pequeno (sem treinos nem pesagens), ou imprima como PDF limpo. Importar mescla, então o plano de quem recebe nunca é sobrescrito
- 🔧 **Filtre por equipamento** — limite a biblioteca ao que você tem; as opções se adaptam ao que escolheu, então toda combinação na tela tem resultados
- ✨ **Seus próprios exercícios** — um nome e uma parte do corpo bastam; funcionam como os nativos em todo lugar, com descrição opcional no lugar da animação
- 🟩 **Heatmap de atividade** — visão anual estilo GitHub, sombreada por tempo de treino
- 💪 **Mapa muscular** — diagrama corporal (frente e costas) sombreado pelo volume de trabalho de cada músculo, por semana, mês ou histórico total. Mostra os músculos que você *não* treinou no período, pré-visualiza o que uma rotina trabalha enquanto monta, e exibe o que acabou de treinar. Figura masculina ou feminina, você escolhe
- 🔔 **Notificações push** — alertas do temporizador de descanso mesmo com o app fechado, mais lembrete opcional nos dias com treino planejado mas não registrado. Opt-in por perfil; chaves geradas no primeiro uso, nada para configurar
- 🤖 **Treinador IA** (opcional) — uma IA que *cria* seu plano e ajusta com base no que você realmente registra. Um questionário rápido gera um plano semanal completo que você refina em linguagem natural; sob demanda ou agendado, ela lê suas estagnações, avaliações de esforço, aderência e tendência de peso corporal e propõe **alterações pontuais e explicadas** que você aceita uma a uma. Escolha o Claude Agent SDK oficial ou o OpenAI Codex CLI incluído com login via ChatGPT; fica desligado até o dono da instância ativar, exige consentimento separado de cada perfil, e nunca muda nada sem sua aprovação — todo conjunto de alterações é versionado e reversível. O motor de progressão continua responsável pelos pesos entre sessões. **[Guia completo →](docs/AI_COACH.md)**
- 🔑 **Passkeys, não senhas** — login por Face ID / Touch ID / digital; cada perfil mantém seus próprios dados, sincronizados entre dispositivos
- 🛠️ **Painel de administração** (opcional) — para quem roda a instância: quem está treinando agora, histórico por usuário, desativar contas e cadastro apenas por convite. Desativado por padrão, então uma instância nova fica aberta sem admin
- 🎨 **Design, não gambiarra** — temas claro/escuro e 8 cores de destaque salvas no seu perfil, com ícones desenhados à mão em vez de emoji, para ficar igual em qualquer celular
- 🌍 **12 idiomas** — tradução completa da interface (EN, DE, ES, FR, IT, PT-BR, PL, TR, RU, ZH, KO, HI); instruções de exercícios localizadas em 10 deles, carregadas sob demanda para o app continuar rápido
- 📥 **Traga seu histórico** — importe do **FitNotes** (Android e iOS), **Strong** e **Hevy**, ou peso corporal direto de um export do **Apple Health**. Nomes de exercícios são cruzados com a biblioteca e o que não for reconhecido vira exercício personalizado, então nada do arquivo é perdido
- 📦 **Seu para sempre** — export/import JSON com um toque, modo convidado, **zero telemetria**
- 📱 **App Android standalone** — o rastreador completo como APK para instalar manualmente: sem conta, sem servidor, dados no celular, lembretes nativos de treino ([download](https://opengym.duarte-santos.ch))

## Início rápido (self-host)

Você precisa do [Docker](https://docs.docker.com/get-docker/) com Compose.

```bash
git clone https://github.com/dougllassillva27/openGym
cd openGym
cp .env.example .env
docker compose pull   # baixa imagens prontas (amd64 + arm64) — pule para compilar do zero
docker compose up -d
```

Abra **http://localhost:8080**, clique em **Criar perfil**, e pronto. O primeiro acesso baixa as mídias dos exercícios (~140 MB) uma única vez. Prefere compilar as imagens em vez de baixar do `ghcr.io`? Pule o passo `pull` e rode `docker compose up -d --build` — você não precisa de Node nem de build local de nenhum jeito.

> Quer acessar pelo celular via internet com passkeys? Você vai precisar de um domínio HTTPS —
> duas linhas no `.env`. Veja **[docs/SELF_HOSTING.md](docs/SELF_HOSTING.md)**.

## App mobile (sem servidor nenhum)

O mesmo código também compila um **app mobile standalone** (Capacitor): sem conta, sem sync,
sem backend — tudo fica no celular, com lembretes nativos de dia de treino e backup via menu de
compartilhamento. Self-hosting te dá sincronização multi-dispositivo e perfis para amigos e família;
o app mobile é a versão instala-e-usa.

- **Android:** [**baixe o APK**](https://opengym.duarte-santos.ch) e instale manualmente —
  o openGym não está na Play Store de propósito. Ou compile você mesmo: **[docs/MOBILE.md](docs/MOBILE.md)**.
- **iPhone:** A Apple não permite instalar apps fora da App Store, então não há download iOS.
  Faça self-host e adicione à tela inicial pelo Safari (é um PWA completo), ou compile o app
  nativo no seu próprio dispositivo pelo Xcode — veja **[docs/MOBILE.md](docs/MOBILE.md)**.

## Como funciona

```
┌──────────────┐        ┌──────────────────────────────┐
│  Seu celular │──HTTPS─▶│  web  (nginx)                │
│  / notebook  │        │   ├─ serve o app compilado   │
└──────────────┘        │   └─ proxy /api ──────────┐  │
                        └──────────────────────────────┘│
                                                        ▼
                                        ┌──────────────────────────┐
                                        │  api  (Node + WebAuthn)  │
                                        │   └─ ./data (JSON files) │
                                        └──────────────────────────┘
```

- **frontend/** — React + Vite (React Router + Zustand), compilado para arquivos estáticos **dentro do Docker**
- **api/** — Node sem framework, uma dependência (`@simplewebauthn/server`), salvando tudo como arquivos JSON em `./data`
- **web/** — imagem multi-stage que compila o frontend e serve com nginx, fazendo proxy de `/api` para o backend, tudo na **mesma origem** (passkeys exigem isso)

## Seus dados

Ficam em `./data` na sua máquina: `db.json` (perfis + passkeys públicas), `state-<usuario>.json`
(plano, treinos, peso corporal e configurações de cada usuário), e `secret` (chave do cookie de sessão).
**Faça backup de `./data` e você fez backup de tudo.** As chaves privadas das passkeys nunca tocam o
servidor — ficam no hardware seguro do seu celular / seu gerenciador de senhas.

## Configuração

Tudo via `.env` (veja `.env.example`):

| Variável         | O que é                                                  | Padrão                  |
|------------------|----------------------------------------------------------|-------------------------|
| `RP_ID`          | Hostname ao qual as passkeys são vinculadas              | `localhost`             |
| `ORIGIN`         | URL completa de onde o app é servido                     | `http://localhost:8080` |
| `WEB_PORT`       | Porta do host para a interface web                       | `8080`                  |
| `RP_NAME`        | Nome exibido no prompt da passkey                        | `openGym`               |
| `ADMIN_UIDS`     | IDs de usuário com acesso ao painel admin (separados por vírgula) | *(nenhum)*      |
| `INVITE_ONLY`    | Exigir código de convite para criar perfil               | *(desativado)*          |
| `COACH_DISABLED` | Força o Treinador IA desligado, independente do painel admin | *(não definido)*   |

As chaves de notificação push são geradas no primeiro uso e salvas em `./data/vapid.json` — nada para configurar.

O **Treinador IA** não precisa de nenhuma variável `.env`: o Claude Agent SDK e o OpenAI Codex CLI vêm dentro da imagem da API. Um admin pode adicionar um token de setup do Claude Code ou completar o login por device-code do ChatGPT no painel. Veja [o guia do Treinador IA](docs/AI_COACH.md),
[o guia de self-hosting](docs/SELF_HOSTING.md#8-the-ai-coach-optional), e os tutoriais de configuração para [Claude](Claude-setup-instructions.md) e [ChatGPT/Codex](ChatGPT-setup-instructions.md).

## Roadmap

Aproximado, guiado pela comunidade — ideias e PRs bem-vindos:

- [x] App mobile standalone — APK Android para instalação manual ([download](https://opengym.duarte-santos.ch)); no iOS como PWA self-hosted (sem planos para lojas)
- [x] Programas de progressão automática (linear, Greyskull LP, progressão dupla) com estagnações e deloads
- [x] 1RM estimado por exercício
- [ ] Programação por porcentagem / training-max (estilo 5/3/1) sobre o motor de progressão
- [x] Treinador IA — criação de planos e revisões baseadas em feedback, via agente CLI rodando no seu servidor
- [ ] Mais planos iniciais (upper/lower, full-body, 5×5)
- [x] Importadores do FitNotes / Strong / Hevy (incluindo o RPE que registram), e peso corporal do Apple Health
- [x] Esforço por série — RIR ou RPE, a escala que você preferir
- [ ] Medidas corporais (cintura, braços…) junto com peso
- [ ] Notas por exercício e calculadora de anilhas
- [ ] Instruções de exercícios em alemão e português (interface traduzida; dataset upstream ainda não inclui)

## Tecnologias

React 19 + Vite (React Router, Zustand) · Node (sem framework) · nginx · Docker Compose ·
WebAuthn · dados de exercícios de [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset).
Sem servidor de banco de dados, sem dependências de nuvem — o frontend compila dentro do Docker, então
self-hosting é um único comando `docker compose up`.

A lógica de treino — regras de progressão, estimativa de 1RM, leitura de sessões registradas —
vive em funções puras em `frontend/src/lib/` com testes ao lado: `npm test` em
`frontend/`. Vitest é dependência de dev; o app em si não embarca dependências de runtime além do
React, o router e o Zustand.

## Comunidade

- **[Q&A](https://github.com/DuarteSantos8/openGym/discussions/categories/q-a)** — ajuda com
  self-hosting, problemas de passkey/login, "como faço…". A maioria dos problemas de login é
  incompatibilidade entre `RP_ID` e `ORIGIN`.
- **[Ideias](https://github.com/DuarteSantos8/openGym/discussions/categories/ideas)** — funcionalidades
  para discutir antes de alguém escrever código.
- **[Show and tell](https://github.com/DuarteSantos8/openGym/discussions/categories/show-and-tell)**
  — seu setup, seus templates de plano, o que construiu em cima.
- **[Issues](https://github.com/DuarteSantos8/openGym/issues)** — bugs e trabalho já aprovado.

## Contribuindo

Issues e PRs bem-vindos — veja [CONTRIBUTING.md](CONTRIBUTING.md). Boas primeiras issues: mais planos
iniciais, idiomas para dados de exercícios, importação de outros rastreadores. **Uma ⭐ ajuda mais pessoas a encontrarem o projeto.**

O openGym é gratuito e continua gratuito: AGPL, sem assinatura, sem plano pago, nada escondido para
patrocinadores. Se substituiu um app pago para você e quiser contribuir, o botão Sponsor no topo da
página está lá — uma estrela, um bug report ou um PR vale tanto quanto.

## Licença

[GNU AGPL v3.0](LICENSE) — software livre e open source. Você pode fazer self-host, usar, modificar e compartilhar;
se rodar uma versão modificada como serviço de rede, deve oferecer o código dessa versão sob a mesma licença.
Ninguém pode transformar o openGym num produto fechado e proprietário.

Imagens/GIFs de exercícios são baixados do dataset upstream e mantêm seus próprios termos — veja [NOTICE.md](NOTICE.md).
