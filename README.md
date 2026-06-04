# Digital Mao - Real-Time Multiplayer Card Game

A browser-based implementation of the card game Mao with an LLM-powered judge, dynamic rules engine, and real-time multiplayer capabilities.

## Project Overview

**Status:** Design Complete - Ready for Implementation
**Complexity Tier:** COMPLEX
**GitHub Repository:** [mterry/digital-mao](https://github.com/mterry/digital-mao)
**Monday.com Board:** [Digital Mao Game - Development](https://ibm.monday.com/boards/18415666999)

### What is Mao?

Mao is a card game where the rules are secret and players must discover them through gameplay. The unique twist: players cannot explain the rules to new players. This digital implementation uses an LLM as an intelligent judge to enforce rules consistently while maintaining the mystery.

## Architecture Highlights

- **Real-time Multiplayer:** WebSocket-based communication for instant gameplay
- **LLM Judge:** AI-powered rule enforcement with learning capabilities
- **Dynamic Rules Engine:** All rules compiled at runtime (no hard-coded logic)
- **Transactional State:** PostgreSQL for ACID-compliant game state
- **Knowledge Graph:** Neo4j for LLM context and precedent storage
- **Contract-First:** All components built from formal specifications

## Technology Stack

### Frontend
- React + TypeScript
- Socket.io-client for WebSocket
- Tailwind CSS for styling
- Custom card game UI components

### Backend
- Node.js + Express
- Socket.io for real-time communication
- PostgreSQL for game state
- Neo4j for knowledge graph
- Bull (Redis) for event queue

### AI/ML
- OpenAI GPT-4 or Anthropic Claude for LLM Judge
- Custom rule compiler for natural language → executable rules

## Project Structure

```
mao/
├── docs/                    # Project documentation
├── specs/                   # Contracts and specifications
│   ├── contracts/          # OpenAPI, AsyncAPI, Component contracts
│   └── templates/          # Contract templates
├── src/
│   ├── client/             # Frontend React application
│   ├── server/             # Backend Node.js services
│   └── shared/             # Shared types and utilities
├── tools/                   # Development tools and scripts
└── .github/workflows/      # CI/CD pipelines
```

## Development Workflow

This project follows a **CONTRACT-FIRST** approach with specialist delegation:

1. **Innovation Designer** - User stories, personas, journey maps
2. **Solutions Architect** - Formal contracts (OpenAPI, AsyncAPI, JSON Schema)
3. **UI/UX Designer** - Design system and component specifications
4. **Frontend Developer** - Client implementation with TDD
5. **Backend Developer** - Server implementation with TDD
6. **Platform Engineer** - Infrastructure and deployment

## Key Features

### For Players
- Real-time multiplayer card game
- Integrated chat for communication
- Visual card interface
- Automatic rule enforcement
- Progressive rule discovery

### For Rule Creators (Winners)
- Natural language rule proposals
- LLM-powered rule compilation
- Confirmation workflow
- Rule activation feedback

### For the LLM Judge
- Context-aware rule enforcement
- Learning from creator feedback
- Precedent-based decisions
- Cryptic penalty messages (maintains mystery)

## Getting Started

*Documentation will be added as specialists complete their work.*

## Contributing

This project uses a structured workflow with specialist modes. See `docs/CONTRIBUTING.md` for details.

## License

*To be determined*

## Contact

Project tracked on Monday.com: https://ibm.monday.com/boards/18415666999