feat(i18n): adiciona traducao pt-br de exercicios

- Gera exercises-pt.js com 1324 nomes traduzidos + aliases de busca via script Python usando qwenbridge
- exercises.js enriquece EXDB em runtime com .nPt e .aliases, exporta exName()
- Library.jsx e sheets.jsx buscam tambem em nPt e aliases (com Array.isArray guard)
- Todos os displays usam exName() para renderizar nome traduzido quando idioma=pt
- i18n.js auto-detecta browser language como fallback (pt-BR default para navegadores em portugues)
- docker-compose.yml binda porta web em 127.0.0.1:8081 (sem exposicao publica)
- .env configurado com RP_ID/ORIGIN para passkeys no dominio HTTPS
