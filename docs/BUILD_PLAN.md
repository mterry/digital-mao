# Build Coordination Plan v1.0.0

## Overview
This plan coordinates the implementation phase across specialist modes, ensuring contract compliance and efficient delivery of the Digital Mao MVP.

**Project:** Digital Mao - Online Multiplayer Card Game  
**Phase:** Implementation (Post-Contract)  
**Target Release:** MVP (Release 1)  
**Timeline:** 4 weeks (estimated)

---

## Implementation Strategy

### Contract-First Principles
1. **All implementations must satisfy contracts** - No deviations without architect approval
2. **Contracts are immutable during implementation** - Changes require new contract version
3. **Validation is continuous** - Contract tests run on every commit
4. **Diagrams guide implementation** - Sequence diagrams define exact flows

### Parallel Workstreams
- **Frontend & Backend can work in parallel** using contracts as interface
- **Infrastructure setup happens first** to enable deployment
- **Integration testing happens continuously** as components complete

---

## Phase 1: Infrastructure Setup (Week 1)

### Owner: Platform Engineer Mode

### Deliverables
1. **Development Environment**
   - Docker Compose setup for local development
   - PostgreSQL database with schema from [`specs/diagrams/source/database-schema.mmd`](specs/diagrams/source/database-schema.mmd)
   - Redis for session management
   - Development SSL certificates

2. **CI/CD Pipeline**
   - GitHub Actions workflow
   - Contract validation on PR (Spectral, AsyncAPI CLI, AJV)
   - Automated testing (unit, integration, e2e)
   - Deployment to staging environment

3. **Monitoring & Logging**
   - Application logging (Winston/Pino)
   - Error tracking (Sentry)
   - Performance monitoring (New Relic/DataDog)
   - WebSocket connection monitoring

### Contract References
- Database schema: [`specs/diagrams/source/database-schema.mmd`](specs/diagrams/source/database-schema.mmd)
- Architecture: [`specs/diagrams/rendered/c4-container.html`](specs/diagrams/rendered/c4-container.html)

### Success Criteria
- ✅ Local environment runs with `docker-compose up`
- ✅ CI/CD pipeline validates all contracts
- ✅ Database schema matches diagram
- ✅ Monitoring dashboards operational

### Handoff to Next Phase
- Development environment ready for frontend/backend teams
- CI/CD validates contract compliance automatically
- Deployment pipeline ready for staging releases

---

## Phase 2: Backend Core (Week 1-2)

### Owner: Backend Developer Mode

### Implementation Order

#### 2.1 Database Layer
**Contracts:** All JSON Schemas  
**Priority:** Critical Path

- Implement PostgreSQL schema from [`specs/diagrams/source/database-schema.mmd`](specs/diagrams/source/database-schema.mmd)
- Create TypeORM/Prisma entities matching:
  - [`specs/contracts/card-schema-v1.0.0.json`](specs/contracts/card-schema-v1.0.0.json)
  - [`specs/contracts/player-schema-v1.0.0.json`](specs/contracts/player-schema-v1.0.0.json)
  - [`specs/contracts/game-state-schema-v1.0.0.json`](specs/contracts/game-state-schema-v1.0.0.json)
  - [`specs/contracts/rule-schema-v1.0.0.json`](specs/contracts/rule-schema-v1.0.0.json)
  - [`specs/contracts/compiled-rule-schema-v1.0.0.json`](specs/contracts/compiled-rule-schema-v1.0.0.json)
  - [`specs/contracts/enforcement-case-schema-v1.0.0.json`](specs/contracts/enforcement-case-schema-v1.0.0.json)
  - [`specs/contracts/chat-message-schema-v1.0.0.json`](specs/contracts/chat-message-schema-v1.0.0.json)
- Write database migrations
- Create repository layer with contract validation

**Validation:** Run AJV validation on all database operations

#### 2.2 REST API Implementation
**Contracts:** OpenAPI Specifications  
**Priority:** Critical Path

Implement in this order (dependency-based):

1. **Game Management API** - [`specs/contracts/game-management-api-v1.0.0.yaml`](specs/contracts/game-management-api-v1.0.0.yaml)
   - POST /games (create game)
   - GET /games (list games)
   - POST /games/{gameId}/join (join game)
   - POST /games/{gameId}/start (start game)
   - POST /games/{gameId}/actions/play-card (play card)
   - POST /games/{gameId}/actions/draw-card (draw card)
   - GET /games/{gameId}/state (get state)

2. **Rule Management API** - [`specs/contracts/rule-management-api-v1.0.0.yaml`](specs/contracts/rule-management-api-v1.0.0.yaml)
   - POST /rules/propose (propose rule)
   - GET /rules/{ruleId} (get rule)
   - POST /rules/{ruleId}/activate (activate rule)
   - GET /games/{gameId}/rules (list active rules)

3. **LLM Judge API** - [`specs/contracts/llm-judge-api-v1.0.0.yaml`](specs/contracts/llm-judge-api-v1.0.0.yaml)
   - POST /judge/compile-rule (compile natural language to executable)
   - POST /judge/evaluate-action (evaluate player action)

**Validation:** 
- OpenAPI validation with Spectral
- Contract tests with Pact
- Postman collection for manual testing

#### 2.3 WebSocket Server
**Contracts:** AsyncAPI Specifications  
**Priority:** Critical Path

Implement WebSocket channels from:
- [`specs/contracts/game-events-v1.0.0.yaml`](specs/contracts/game-events-v1.0.0.yaml)
- [`specs/contracts/chat-events-v1.0.0.yaml`](specs/contracts/chat-events-v1.0.0.yaml)
- [`specs/contracts/rule-events-v1.0.0.yaml`](specs/contracts/rule-events-v1.0.0.yaml)

**Implementation:**
- Socket.io server with authentication
- Room-based game channels
- Event broadcasting matching AsyncAPI schemas
- Connection state management

**Validation:** AsyncAPI CLI validation on all events

#### 2.4 LLM Integration
**Contracts:** [`specs/contracts/llm-judge-api-v1.0.0.yaml`](specs/contracts/llm-judge-api-v1.0.0.yaml)  
**Priority:** High

- OpenAI API integration for rule compilation
- Prompt engineering for rule interpretation
- Context management for action evaluation
- Fallback handling for LLM failures
- Response caching for performance

**Validation:** Unit tests with mocked LLM responses

### Success Criteria
- ✅ All REST endpoints return responses matching OpenAPI schemas
- ✅ All WebSocket events match AsyncAPI schemas
- ✅ Database entities match JSON schemas
- ✅ LLM judge compiles rules and evaluates actions
- ✅ 80%+ unit test coverage
- ✅ All contract tests pass

### Handoff to Frontend
- REST API deployed to staging with Swagger UI
- WebSocket server accepting connections
- Test data seeded for frontend development
- Postman collection shared for API testing

---

## Phase 3: Frontend Implementation (Week 2-3)

### Owner: Frontend Developer Mode

### Prerequisites
- Backend APIs deployed to staging
- Design system from UI/UX Designer (if needed)
- Component contracts reviewed

### Implementation Order

#### 3.1 Project Setup
- Create React app with TypeScript
- Set up state management (Redux Toolkit/Zustand)
- Configure WebSocket client (Socket.io-client)
- Set up routing (React Router)
- Configure API client with OpenAPI types

#### 3.2 Core Components
**Contracts:** Component Specifications  
**Priority:** Critical Path

Implement in this order:

1. **GameBoard Component** - [`specs/contracts/gameboard-component-v1.0.0.json`](specs/contracts/gameboard-component-v1.0.0.json)
   - Props: gameState, currentPlayer, onCardClick
   - State: selectedCard, animations
   - Events: cardPlayed, cardDrawn
   - Accessibility: ARIA labels, keyboard navigation
   - Performance: < 100ms render, 60fps animations

2. **PlayerHand Component** - [`specs/contracts/playerhand-component-v1.0.0.json`](specs/contracts/playerhand-component-v1.0.0.json)
   - Props: cards, playableCards, onCardSelect
   - State: selectedCard, sortOrder
   - Events: cardSelected, cardPlayed
   - Accessibility: Keyboard card selection, screen reader
   - Performance: < 50ms re-render

3. **ChatPanel Component** - [`specs/contracts/chatpanel-component-v1.0.0.json`](specs/contracts/chatpanel-component-v1.0.0.json)
   - Props: messages, onSendMessage
   - State: inputValue, isTyping
   - Events: messageSent, typingStarted
   - Accessibility: ARIA live regions, keyboard navigation
   - Performance: Virtual scrolling for 1000+ messages

4. **RuleProposal Component** - [`specs/contracts/ruleproposal-component-v1.0.0.json`](specs/contracts/ruleproposal-component-v1.0.0.json)
   - Props: onSubmit, compilationStatus
   - State: ruleText, step (propose/compile/review)
   - Events: ruleProposed, ruleActivated
   - Accessibility: Form validation, error announcements
   - Performance: Debounced validation

#### 3.3 API Integration
- REST API client using OpenAPI-generated types
- WebSocket event handlers matching AsyncAPI schemas
- State synchronization between REST and WebSocket
- Optimistic updates with rollback on error

#### 3.4 Game Flows
**Reference:** Sequence Diagrams

Implement flows matching:
- Card play: [`specs/diagrams/rendered/card-play-flow.html`](specs/diagrams/rendered/card-play-flow.html)
- Rule compilation: [`specs/diagrams/rendered/rule-compilation-flow.html`](specs/diagrams/rendered/rule-compilation-flow.html)
- Penalty enforcement: [`specs/diagrams/rendered/penalty-enforcement-flow.html`](specs/diagrams/rendered/penalty-enforcement-flow.html)
- Game start: [`specs/diagrams/rendered/game-start-flow.html`](specs/diagrams/rendered/game-start-flow.html)

### Success Criteria
- ✅ All components match contract specifications
- ✅ All props/state/events as specified
- ✅ Accessibility requirements met (WCAG 2.1 AA)
- ✅ Performance requirements met (< 100ms render)
- ✅ WebSocket events handled correctly
- ✅ 80%+ component test coverage
- ✅ Storybook documentation for all components

### Handoff to Integration
- Frontend deployed to staging
- All components documented in Storybook
- E2E test scenarios identified
- Known issues documented

---

## Phase 4: Integration & Testing (Week 3-4)

### Owner: Backend Developer + Frontend Developer (Coordinated)

### Integration Points

#### 4.1 API Integration Testing
- Test all REST endpoints with real frontend
- Validate request/response schemas match contracts
- Test error handling and edge cases
- Performance testing (load, stress)

#### 4.2 WebSocket Integration Testing
- Test all event channels with real clients
- Validate event payloads match AsyncAPI schemas
- Test connection handling (disconnect, reconnect)
- Test room-based broadcasting

#### 4.3 End-to-End Workflows
Test complete user journeys:
1. Create game → Join → Start → Play cards → Win round
2. Propose rule → Compile → Review → Activate → Enforce
3. Chat → Receive messages → Judge feedback
4. Penalty → Draw cards → Continue game
5. Player disconnect → Reconnect → Resume game

#### 4.4 Contract Compliance Validation
- Run Spectral on all API responses
- Run AsyncAPI CLI on all WebSocket events
- Run AJV on all data models
- Verify all diagrams match implementation

### Success Criteria
- ✅ All integration tests pass
- ✅ All contract validations pass
- ✅ All E2E workflows complete successfully
- ✅ Performance benchmarks met
- ✅ Security scan passes (no vulnerabilities)
- ✅ Accessibility audit passes (WCAG 2.1 AA)

---

## Phase 5: Deployment & Launch (Week 4)

### Owner: Platform Engineer Mode

### Deployment Steps

1. **Production Infrastructure**
   - Provision production servers
   - Configure production database
   - Set up CDN for static assets
   - Configure SSL certificates
   - Set up backup and disaster recovery

2. **Production Deployment**
   - Deploy backend to production
   - Deploy frontend to CDN
   - Run smoke tests
   - Monitor error rates and performance

3. **Launch Checklist**
   - ✅ All contracts validated in production
   - ✅ Monitoring dashboards operational
   - ✅ Error tracking configured
   - ✅ Backup systems tested
   - ✅ Rollback plan documented
   - ✅ Support documentation ready

### Success Criteria
- ✅ Production deployment successful
- ✅ All systems operational
- ✅ Performance meets SLAs
- ✅ Zero critical bugs
- ✅ Monitoring shows healthy metrics

---

## Contract Compliance Checkpoints

### Continuous Validation
- **Every PR:** Contract validation in CI/CD
- **Every Deploy:** Contract tests run in staging
- **Every Release:** Full contract audit

### Validation Tools
- **OpenAPI:** Spectral linter
- **AsyncAPI:** AsyncAPI CLI validator
- **JSON Schema:** AJV validator
- **Components:** Jest + React Testing Library
- **E2E:** Playwright with contract assertions

### Violation Handling
1. **Detection:** Automated validation catches violation
2. **Block:** PR/deployment blocked until resolved
3. **Resolution:** Fix implementation OR update contract (with architect approval)
4. **Verification:** Re-run validation

---

## Risk Management

### Technical Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| LLM API rate limits | High | Implement caching, fallback rules |
| WebSocket scaling | Medium | Use Redis pub/sub, horizontal scaling |
| Database performance | Medium | Optimize queries, add indexes |
| Frontend performance | Low | Code splitting, lazy loading |

### Schedule Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Backend delays | High | Frontend uses mock data initially |
| Integration issues | Medium | Daily sync meetings, early integration |
| Contract changes | High | Freeze contracts during implementation |

---

## Communication Plan

### Daily Standups
- **Time:** 10:00 AM EST
- **Attendees:** All specialist modes
- **Format:** What's done, what's next, blockers

### Weekly Reviews
- **Time:** Friday 2:00 PM EST
- **Attendees:** All specialists + architect
- **Format:** Demo, contract compliance review, next week planning

### Slack Channels
- `#mao-backend` - Backend development
- `#mao-frontend` - Frontend development
- `#mao-integration` - Integration issues
- `#mao-contracts` - Contract questions/changes

---

## Success Metrics

### Quality Metrics
- Contract compliance: 100%
- Test coverage: > 80%
- Bug count: < 10 critical bugs
- Performance: All SLAs met

### Delivery Metrics
- On-time delivery: Week 4
- Scope completion: 100% of MVP stories
- Technical debt: < 5% of codebase

---

## Next Steps

1. **Platform Engineer:** Set up infrastructure (Week 1)
2. **Backend Developer:** Implement APIs and WebSocket (Week 1-2)
3. **Frontend Developer:** Implement components and flows (Week 2-3)
4. **All Teams:** Integration testing (Week 3-4)
5. **Platform Engineer:** Production deployment (Week 4)

---

**Plan Version:** 1.0.0  
**Created:** 2026-06-01  
**Status:** ✅ READY FOR EXECUTION  
**Next Review:** End of Week 1