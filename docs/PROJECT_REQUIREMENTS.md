# Digital Mao - Project Requirements

## Executive Summary

Build a browser-based, real-time multiplayer implementation of the card game Mao with an LLM-powered judge that enforces dynamically compiled rules while maintaining the game's core mystery.

## Business Objectives

1. Create an engaging digital version of Mao that preserves the game's unique learning-through-failure mechanic
2. Demonstrate innovative use of LLM technology for game rule enforcement
3. Provide a scalable, production-ready multiplayer gaming platform
4. Enable natural language rule creation by players

## User Personas

### Primary Users
- **Card Game Enthusiasts:** Players familiar with traditional card games seeking novel experiences
- **Mao Veterans:** Experienced Mao players wanting to play remotely
- **New Players:** People curious about Mao who want to learn through gameplay

### Secondary Users
- **Rule Creators:** Winners who add new rules to increase complexity
- **Observers:** Spectators watching games to learn patterns

## Core Requirements

### Functional Requirements

#### FR1: Real-Time Multiplayer Gameplay
- Support 2-8 players per game
- WebSocket-based communication for <100ms latency
- Synchronized game state across all clients
- Automatic reconnection handling

#### FR2: Card Game Mechanics
- Standard 52-card deck
- Card matching rules (suit or rank)
- Special card effects (8s change suit, Aces reverse direction, Queens skip)
- Turn-based gameplay with automatic turn advancement
- Win condition: first player to empty hand

#### FR3: Dynamic Rules Engine
- All rules compiled at runtime (zero hard-coded rules)
- LLM-powered natural language → executable rule compilation
- Rule activation/deactivation
- Rule priority system for conflict resolution
- Extensible evaluator system for new rule types

#### FR4: LLM Judge System
- Automatic rule enforcement for all active rules
- Context-aware judgment using recent game history
- Learning from creator feedback on ambiguous cases
- Precedent-based decision making
- Cryptic penalty messages (no explicit rule explanations)

#### FR5: Chat Integration
- Real-time chat alongside gameplay
- Chat messages analyzed for rule compliance
- System messages for game events
- Judge messages for penalties and feedback

#### FR6: Rule Proposal System
- Winners can propose new rules in natural language
- LLM compiles rules into executable format
- Confirmation workflow with rule creator
- Rule activation upon approval

#### FR7: Game State Management
- Transactional database (PostgreSQL) for consistency
- ACID guarantees for all state changes
- Complete audit trail of game events
- Rollback capability for failed operations

#### FR8: Knowledge Graph for LLM Context
- Store enforcement cases and precedents
- Pattern matching for similar situations
- Rule dependency tracking
- Learning data separate from game state

### Non-Functional Requirements

#### NFR1: Performance
- Game state updates: <50ms
- LLM judgment: <2 seconds
- Support 100 concurrent games
- Database queries: <10ms p95

#### NFR2: Scalability
- Horizontal scaling for game servers
- Stateless application servers
- Shared state via Redis/PostgreSQL
- Load balancing across instances

#### NFR3: Reliability
- 99.9% uptime target
- Automatic failover for database
- Graceful degradation if LLM unavailable
- Data persistence and backup

#### NFR4: Security
- Secure WebSocket connections (WSS)
- Input validation and sanitization
- Rate limiting on API endpoints
- No sensitive data in client code

#### NFR5: Maintainability
- Contract-first architecture
- Comprehensive test coverage (>90%)
- Clear separation of concerns
- Extensive documentation

#### NFR6: Usability
- Intuitive card game interface
- Clear visual feedback for actions
- Responsive design (desktop and tablet)
- Accessibility compliance (WCAG 2.1 AA)

## Technical Constraints

### Must Use
- PostgreSQL for transactional game state
- Neo4j for knowledge graph
- WebSocket for real-time communication
- LLM API (OpenAI or Anthropic) for judge

### Must Not Use
- Hard-coded game rules
- Synchronous blocking operations
- Client-side game state as source of truth
- Unencrypted communication

## Success Criteria

### Minimum Viable Product (MVP)
1. 2-4 player games functional
2. Basic card matching rules working
3. LLM judge enforcing at least 3 custom rules
4. Chat integration complete
5. Rule proposal and compilation working
6. Transactional state management operational

### Full Release
1. Support 2-8 players
2. All special card effects implemented
3. LLM judge with learning capability
4. Knowledge graph storing precedents
5. Complete test coverage
6. Production deployment ready
7. Performance targets met

## Out of Scope (V1)

- Mobile app (mobile web only)
- Tournament mode
- Player rankings/leaderboards
- Replay system
- Custom card decks
- AI players (human-only)
- Voice chat
- Video streaming

## Dependencies

### External Services
- LLM API (OpenAI GPT-4 or Anthropic Claude)
- PostgreSQL database
- Neo4j database
- Redis for event queue

### Internal Dependencies
- Innovation Designer: User stories and personas
- Solutions Architect: Complete contract suite
- UI/UX Designer: Design system and mockups
- Frontend Developer: Client implementation
- Backend Developer: Server implementation
- Platform Engineer: Infrastructure and deployment

## Timeline Estimate

**Total Estimated Effort:** 8-12 weeks

- Week 1-2: Requirements, user stories, contracts
- Week 3-4: Design system and architecture
- Week 5-8: Core implementation (frontend + backend)
- Week 9-10: LLM integration and testing
- Week 11-12: Platform setup and deployment

## Risk Assessment

### High Risk
- LLM API reliability and latency
- Complex rule interactions and conflicts
- Real-time synchronization at scale

### Medium Risk
- Knowledge graph query performance
- Rule compilation accuracy
- WebSocket connection stability

### Low Risk
- Basic card game mechanics
- Database transactions
- Frontend UI implementation

## Acceptance Criteria

A game is considered complete when:
1. Players can join a game and see synchronized state
2. Players can play cards following matching rules
3. Chat messages are sent and received in real-time
4. LLM judge correctly enforces at least 3 custom rules
5. Winners can propose and activate new rules
6. All game state changes are transactional
7. System handles player disconnections gracefully
8. Performance targets are met under load testing

## Appendix

### Glossary
- **Mao:** A card game where rules are secret
- **LLM Judge:** AI system that enforces rules
- **Rule Compiler:** Converts natural language to executable rules
- **Knowledge Graph:** Neo4j database storing LLM context
- **Precedent:** Past enforcement case used for future decisions
- **Contract:** Formal specification (OpenAPI, AsyncAPI, JSON Schema)

### References
- [Mao Card Game Rules](https://en.wikipedia.org/wiki/Mao_(card_game))
- [OpenAPI Specification](https://swagger.io/specification/)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/v2.6.0)
- [JSON Schema](https://json-schema.org/)