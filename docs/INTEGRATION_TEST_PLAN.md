# Integration Test Plan v1.0.0

## Overview
This plan defines the integration testing strategy to validate contract compliance, end-to-end workflows, performance, and security for the Digital Mao MVP.

**Project:** Digital Mao - Online Multiplayer Card Game  
**Test Phase:** Integration & E2E Testing  
**Target:** MVP (Release 1)  
**Test Environment:** Staging (mirrors production)

---

## Testing Strategy

### Test Pyramid
```
        /\
       /E2E\         10% - Full user journeys
      /------\
     /Contract\      30% - API/Event contract tests
    /----------\
   /Integration \    30% - Component integration
  /--------------\
 /  Unit Tests   \   30% - Individual functions
/------------------\
```

### Contract-First Testing
1. **Contract validation is mandatory** - All tests verify contract compliance
2. **Contracts define test cases** - Test scenarios derived from contracts
3. **Automated validation** - Contract tests run on every commit
4. **Continuous verification** - Production monitoring validates contracts

---

## Test Categories

### 1. Contract Validation Tests

#### 1.1 JSON Schema Validation
**Tool:** AJV (Another JSON Schema Validator)  
**Frequency:** Every API call, every event

**Test Cases:**
- Validate all API request bodies against schemas
- Validate all API response bodies against schemas
- Validate all WebSocket event payloads against schemas
- Validate all database entities against schemas

**Contracts Under Test:**
- [`specs/contracts/card-schema-v1.0.0.json`](specs/contracts/card-schema-v1.0.0.json)
- [`specs/contracts/player-schema-v1.0.0.json`](specs/contracts/player-schema-v1.0.0.json)
- [`specs/contracts/chat-message-schema-v1.0.0.json`](specs/contracts/chat-message-schema-v1.0.0.json)
- [`specs/contracts/rule-schema-v1.0.0.json`](specs/contracts/rule-schema-v1.0.0.json)
- [`specs/contracts/compiled-rule-schema-v1.0.0.json`](specs/contracts/compiled-rule-schema-v1.0.0.json)
- [`specs/contracts/enforcement-case-schema-v1.0.0.json`](specs/contracts/enforcement-case-schema-v1.0.0.json)
- [`specs/contracts/game-state-schema-v1.0.0.json`](specs/contracts/game-state-schema-v1.0.0.json)

**Implementation:**
```typescript
import Ajv from 'ajv';
import cardSchema from '../specs/contracts/card-schema-v1.0.0.json';

const ajv = new Ajv();
const validateCard = ajv.compile(cardSchema);

test('API returns valid card schema', async () => {
  const response = await api.get('/games/123/state');
  const cards = response.data.deck;
  
  cards.forEach(card => {
    const valid = validateCard(card);
    expect(valid).toBe(true);
    if (!valid) console.error(validateCard.errors);
  });
});
```

#### 1.2 OpenAPI Validation
**Tool:** Spectral  
**Frequency:** CI/CD pipeline, pre-deployment

**Test Cases:**
- Validate OpenAPI spec structure
- Validate all endpoints have examples
- Validate all schemas are referenced
- Validate security schemes are defined
- Validate response codes are appropriate

**Contracts Under Test:**
- [`specs/contracts/game-management-api-v1.0.0.yaml`](specs/contracts/game-management-api-v1.0.0.yaml)
- [`specs/contracts/rule-management-api-v1.0.0.yaml`](specs/contracts/rule-management-api-v1.0.0.yaml)
- [`specs/contracts/llm-judge-api-v1.0.0.yaml`](specs/contracts/llm-judge-api-v1.0.0.yaml)

**Implementation:**
```bash
# Run in CI/CD
spectral lint specs/contracts/game-management-api-v1.0.0.yaml
spectral lint specs/contracts/rule-management-api-v1.0.0.yaml
spectral lint specs/contracts/llm-judge-api-v1.0.0.yaml
```

#### 1.3 AsyncAPI Validation
**Tool:** AsyncAPI CLI  
**Frequency:** CI/CD pipeline, pre-deployment

**Test Cases:**
- Validate AsyncAPI spec structure
- Validate all channels have schemas
- Validate all messages have examples
- Validate server configuration

**Contracts Under Test:**
- [`specs/contracts/game-events-v1.0.0.yaml`](specs/contracts/game-events-v1.0.0.yaml)
- [`specs/contracts/chat-events-v1.0.0.yaml`](specs/contracts/chat-events-v1.0.0.yaml)
- [`specs/contracts/rule-events-v1.0.0.yaml`](specs/contracts/rule-events-v1.0.0.yaml)

**Implementation:**
```bash
# Run in CI/CD
asyncapi validate specs/contracts/game-events-v1.0.0.yaml
asyncapi validate specs/contracts/chat-events-v1.0.0.yaml
asyncapi validate specs/contracts/rule-events-v1.0.0.yaml
```

#### 1.4 Component Contract Validation
**Tool:** Jest + React Testing Library  
**Frequency:** Every component test

**Test Cases:**
- Validate component props match contract
- Validate component state matches contract
- Validate component events match contract
- Validate accessibility requirements met
- Validate performance requirements met

**Contracts Under Test:**
- [`specs/contracts/gameboard-component-v1.0.0.json`](specs/contracts/gameboard-component-v1.0.0.json)
- [`specs/contracts/playerhand-component-v1.0.0.json`](specs/contracts/playerhand-component-v1.0.0.json)
- [`specs/contracts/chatpanel-component-v1.0.0.json`](specs/contracts/chatpanel-component-v1.0.0.json)
- [`specs/contracts/ruleproposal-component-v1.0.0.json`](specs/contracts/ruleproposal-component-v1.0.0.json)

**Implementation:**
```typescript
import { render, screen } from '@testing-library/react';
import GameBoard from './GameBoard';
import contract from '../specs/contracts/gameboard-component-v1.0.0.json';

test('GameBoard accepts all contract props', () => {
  const props = {
    gameState: mockGameState,
    currentPlayer: mockPlayer,
    onCardClick: jest.fn(),
  };
  
  // Validate props match contract
  contract.props.forEach(prop => {
    expect(props).toHaveProperty(prop.name);
  });
  
  render(<GameBoard {...props} />);
  expect(screen.getByRole('main')).toBeInTheDocument();
});
```

---

### 2. API Integration Tests

#### 2.1 REST API Tests
**Tool:** Supertest + Jest  
**Frequency:** Every commit

**Test Scenarios:**

##### Game Management API
Reference: [`specs/contracts/game-management-api-v1.0.0.yaml`](specs/contracts/game-management-api-v1.0.0.yaml)

1. **Create Game**
   - POST /games with valid payload
   - Verify response matches schema
   - Verify game created in database
   - Verify game-events WebSocket broadcast

2. **List Games**
   - GET /games
   - Verify response array matches schema
   - Verify pagination works
   - Verify filtering works

3. **Join Game**
   - POST /games/{gameId}/join
   - Verify player added to game
   - Verify game-events broadcast
   - Verify error when game full

4. **Play Card**
   - POST /games/{gameId}/actions/play-card
   - Verify card removed from hand
   - Verify card added to discard pile
   - Verify rule enforcement triggered
   - Verify game-events broadcast

5. **Draw Card**
   - POST /games/{gameId}/actions/draw-card
   - Verify card added to hand
   - Verify deck count decremented
   - Verify game-events broadcast

##### Rule Management API
Reference: [`specs/contracts/rule-management-api-v1.0.0.yaml`](specs/contracts/rule-management-api-v1.0.0.yaml)

1. **Propose Rule**
   - POST /rules/propose
   - Verify rule created with "proposed" status
   - Verify LLM compilation triggered
   - Verify rule-events broadcast

2. **Activate Rule**
   - POST /rules/{ruleId}/activate
   - Verify rule status changed to "active"
   - Verify rule added to game
   - Verify rule-events broadcast

##### LLM Judge API
Reference: [`specs/contracts/llm-judge-api-v1.0.0.yaml`](specs/contracts/llm-judge-api-v1.0.0.yaml)

1. **Compile Rule**
   - POST /judge/compile-rule
   - Verify compiled rule matches schema
   - Verify triggers, conditions, actions present
   - Verify compilation metadata included

2. **Evaluate Action**
   - POST /judge/evaluate-action
   - Verify enforcement case created
   - Verify violation detected correctly
   - Verify penalty applied if needed

**Implementation Example:**
```typescript
import request from 'supertest';
import app from '../src/app';
import { validateCard } from '../src/validators';

describe('Game Management API', () => {
  test('POST /games creates valid game', async () => {
    const response = await request(app)
      .post('/games')
      .send({
        name: 'Test Game',
        maxPlayers: 4,
        settings: { deckType: 'standard' }
      })
      .expect(201);
    
    // Validate response matches contract
    expect(response.body).toHaveProperty('id');
    expect(response.body).toHaveProperty('name', 'Test Game');
    expect(response.body.status).toBe('waiting');
    
    // Validate against JSON schema
    const valid = validateGameState(response.body);
    expect(valid).toBe(true);
  });
});
```

#### 2.2 WebSocket Integration Tests
**Tool:** Socket.io-client + Jest  
**Frequency:** Every commit

**Test Scenarios:**

##### Game Events
Reference: [`specs/contracts/game-events-v1.0.0.yaml`](specs/contracts/game-events-v1.0.0.yaml)

1. **game.created**
   - Connect to WebSocket
   - Create game via REST API
   - Verify event received
   - Verify payload matches schema

2. **game.player-joined**
   - Join game via REST API
   - Verify all players receive event
   - Verify payload includes new player

3. **game.card-played**
   - Play card via REST API
   - Verify all players receive event
   - Verify payload includes card and player

4. **game.penalty-applied**
   - Trigger rule violation
   - Verify penalty event received
   - Verify payload includes enforcement case

##### Chat Events
Reference: [`specs/contracts/chat-events-v1.0.0.yaml`](specs/contracts/chat-events-v1.0.0.yaml)

1. **chat.message**
   - Send chat message
   - Verify all players receive event
   - Verify payload matches schema

2. **chat.judge-feedback**
   - Trigger judge evaluation
   - Verify judge feedback event
   - Verify payload includes reasoning

##### Rule Events
Reference: [`specs/contracts/rule-events-v1.0.0.yaml`](specs/contracts/rule-events-v1.0.0.yaml)

1. **rule.proposed**
   - Propose rule via REST API
   - Verify event received
   - Verify payload includes rule text

2. **rule.compiled**
   - Wait for compilation
   - Verify event received
   - Verify payload includes compiled rule

3. **rule.activated**
   - Activate rule via REST API
   - Verify event received
   - Verify all players notified

**Implementation Example:**
```typescript
import io from 'socket.io-client';

describe('WebSocket Events', () => {
  let socket;
  
  beforeEach((done) => {
    socket = io('http://localhost:3000');
    socket.on('connect', done);
  });
  
  afterEach(() => {
    socket.disconnect();
  });
  
  test('game.card-played event matches schema', (done) => {
    socket.on('game.card-played', (data) => {
      // Validate against AsyncAPI schema
      expect(data).toHaveProperty('gameId');
      expect(data).toHaveProperty('playerId');
      expect(data).toHaveProperty('card');
      expect(validateCard(data.card)).toBe(true);
      done();
    });
    
    // Trigger card play via API
    playCard(gameId, playerId, card);
  });
});
```

---

### 3. End-to-End Workflow Tests

#### 3.1 Complete Game Flow
**Tool:** Playwright  
**Frequency:** Before each release

**Test Scenario:** Full game from creation to completion

**Steps:**
1. Player 1 creates game
2. Player 2 joins game
3. Player 1 starts game
4. Players play cards in sequence
5. Rule violation occurs
6. Penalty applied
7. Player wins round
8. Game ends

**Validation:**
- All UI components render correctly
- All API calls succeed
- All WebSocket events received
- All contracts validated
- Game state consistent throughout

**Reference Diagrams:**
- Card play flow: [`specs/diagrams/rendered/card-play-flow.html`](specs/diagrams/rendered/card-play-flow.html)
- Game start flow: [`specs/diagrams/rendered/game-start-flow.html`](specs/diagrams/rendered/game-start-flow.html)

**Implementation:**
```typescript
import { test, expect } from '@playwright/test';

test('complete game flow', async ({ page, context }) => {
  // Player 1: Create game
  await page.goto('/');
  await page.click('text=Create Game');
  await page.fill('[name="gameName"]', 'Test Game');
  await page.click('text=Create');
  
  const gameUrl = page.url();
  
  // Player 2: Join game (new context)
  const page2 = await context.newPage();
  await page2.goto('/');
  await page2.click('text=Join Game');
  await page2.click(`text=Test Game`);
  
  // Player 1: Start game
  await page.click('text=Start Game');
  
  // Play cards
  await page.click('[data-testid="card-0"]');
  await page2.click('[data-testid="card-0"]');
  
  // Verify game state
  await expect(page.locator('[data-testid="discard-pile"]')).toContainText('2 cards');
});
```

#### 3.2 Rule Lifecycle Flow
**Tool:** Playwright  
**Frequency:** Before each release

**Test Scenario:** Complete rule from proposal to enforcement

**Steps:**
1. Player proposes rule in natural language
2. LLM compiles rule to executable format
3. Player reviews compiled rule
4. Player activates rule
5. Rule enforced on subsequent actions
6. Penalty applied for violation

**Validation:**
- Rule proposal UI works
- Compilation progress shown
- Compiled rule displayed correctly
- Activation succeeds
- Enforcement triggers correctly
- Penalty applied correctly

**Reference Diagrams:**
- Rule compilation flow: [`specs/diagrams/rendered/rule-compilation-flow.html`](specs/diagrams/rendered/rule-compilation-flow.html)
- Penalty enforcement flow: [`specs/diagrams/rendered/penalty-enforcement-flow.html`](specs/diagrams/rendered/penalty-enforcement-flow.html)

#### 3.3 Chat & Judge Feedback Flow
**Tool:** Playwright  
**Frequency:** Before each release

**Test Scenario:** Chat interaction with judge feedback

**Steps:**
1. Player sends chat message
2. Other players receive message
3. Player violates rule
4. Judge provides feedback in chat
5. Player receives penalty explanation

**Validation:**
- Chat messages appear for all players
- Judge messages styled differently
- Penalty explanations clear
- Chat history preserved

---

### 4. Performance Tests

#### 4.1 API Performance
**Tool:** Artillery  
**Frequency:** Weekly, before release

**Test Scenarios:**

1. **Load Test**
   - 100 concurrent users
   - 1000 requests/minute
   - Target: p95 < 200ms

2. **Stress Test**
   - Gradually increase to 500 concurrent users
   - Find breaking point
   - Target: Graceful degradation

3. **Spike Test**
   - Sudden spike to 200 users
   - Target: System recovers

**Implementation:**
```yaml
# artillery-load-test.yml
config:
  target: 'https://staging.mao.example.com'
  phases:
    - duration: 60
      arrivalRate: 10
      name: Warm up
    - duration: 300
      arrivalRate: 100
      name: Load test
scenarios:
  - name: Play game
    flow:
      - post:
          url: '/games'
          json:
            name: 'Load Test Game'
      - post:
          url: '/games/{{ id }}/join'
      - post:
          url: '/games/{{ id }}/actions/play-card'
          json:
            cardId: '{{ cardId }}'
```

#### 4.2 WebSocket Performance
**Tool:** Artillery + Socket.io  
**Frequency:** Weekly, before release

**Test Scenarios:**

1. **Connection Test**
   - 1000 concurrent WebSocket connections
   - Target: All connections stable

2. **Message Throughput**
   - 100 messages/second per connection
   - Target: < 50ms latency

3. **Room Broadcasting**
   - 8 players per game room
   - 100 concurrent games
   - Target: All players receive events

#### 4.3 Frontend Performance
**Tool:** Lighthouse + Playwright  
**Frequency:** Before each release

**Test Scenarios:**

1. **Initial Load**
   - Target: < 2s First Contentful Paint
   - Target: < 3s Time to Interactive

2. **Component Render**
   - Target: < 100ms initial render
   - Target: < 16ms re-render (60fps)

3. **Memory Usage**
   - Target: < 50MB per component
   - Target: No memory leaks

**Implementation:**
```typescript
import { test } from '@playwright/test';
import lighthouse from 'lighthouse';

test('performance audit', async ({ page }) => {
  await page.goto('/');
  
  const result = await lighthouse(page.url(), {
    port: new URL(page.url()).port,
  });
  
  expect(result.lhr.categories.performance.score).toBeGreaterThan(0.9);
});
```

---

### 5. Security Tests

#### 5.1 Authentication Tests
**Tool:** Jest + Supertest  
**Frequency:** Every commit

**Test Scenarios:**

1. **JWT Validation**
   - Valid token accepted
   - Expired token rejected
   - Invalid signature rejected
   - Missing token rejected

2. **WebSocket Authentication**
   - Valid token connects
   - Invalid token rejected
   - Token refresh works

#### 5.2 Authorization Tests
**Tool:** Jest + Supertest  
**Frequency:** Every commit

**Test Scenarios:**

1. **Player Actions**
   - Player can only play own cards
   - Player can only join available games
   - Player cannot modify other players

2. **Spectator Restrictions**
   - Spectator can view game
   - Spectator cannot play cards
   - Spectator cannot propose rules

#### 5.3 Input Validation Tests
**Tool:** Jest + Supertest  
**Frequency:** Every commit

**Test Scenarios:**

1. **SQL Injection**
   - Malicious input rejected
   - Parameterized queries used

2. **XSS Prevention**
   - Chat messages sanitized
   - Rule text sanitized
   - HTML entities escaped

3. **Rate Limiting**
   - Excessive requests blocked
   - Rate limit headers present

#### 5.4 Security Scanning
**Tool:** OWASP ZAP, Snyk  
**Frequency:** Weekly, before release

**Test Scenarios:**

1. **Dependency Scanning**
   - No known vulnerabilities
   - All dependencies up to date

2. **API Security**
   - OWASP Top 10 checks
   - Security headers present

---

### 6. Accessibility Tests

#### 6.1 Automated Accessibility
**Tool:** axe-core + Jest  
**Frequency:** Every commit

**Test Scenarios:**

1. **WCAG 2.1 AA Compliance**
   - No violations detected
   - All components pass

2. **Keyboard Navigation**
   - All interactive elements reachable
   - Focus order logical
   - Focus visible

3. **Screen Reader**
   - ARIA labels present
   - Live regions work
   - Announcements clear

**Implementation:**
```typescript
import { axe, toHaveNoViolations } from 'jest-axe';
expect.extend(toHaveNoViolations);

test('GameBoard is accessible', async () => {
  const { container } = render(<GameBoard {...props} />);
  const results = await axe(container);
  expect(results).toHaveNoViolations();
});
```

#### 6.2 Manual Accessibility
**Tool:** Manual testing with screen readers  
**Frequency:** Before each release

**Test Scenarios:**

1. **NVDA/JAWS Testing**
   - Navigate entire game with screen reader
   - Verify all actions announced
   - Verify game state communicated

2. **Keyboard-Only Testing**
   - Complete game using only keyboard
   - Verify all actions possible
   - Verify shortcuts work

---

## Test Execution Plan

### Continuous Integration (Every Commit)
```bash
# Run in CI/CD pipeline
npm run test:unit           # Unit tests
npm run test:integration    # API integration tests
npm run test:contracts      # Contract validation
npm run test:accessibility  # Accessibility tests
npm run lint                # Code quality
```

### Pre-Deployment (Staging)
```bash
# Run before deploying to staging
npm run test:e2e            # End-to-end tests
npm run test:performance    # Performance tests
npm run test:security       # Security scans
artillery run load-test.yml # Load testing
```

### Pre-Release (Production)
```bash
# Run before production release
npm run test:all            # All tests
npm run audit:security      # Security audit
npm run audit:accessibility # Accessibility audit
lighthouse --view           # Performance audit
```

---

## Test Data Management

### Test Data Strategy
1. **Seed Data:** Consistent test data for development
2. **Factories:** Generate test data programmatically
3. **Fixtures:** Predefined test scenarios
4. **Cleanup:** Reset database after each test

### Test Data Examples
```typescript
// factories/game.factory.ts
export const createTestGame = () => ({
  id: uuid(),
  name: 'Test Game',
  status: 'waiting',
  players: [],
  deck: createStandardDeck(),
  rules: [],
  createdAt: new Date(),
});

// fixtures/games.json
{
  "activeGame": {
    "id": "game-123",
    "status": "active",
    "players": [/* ... */],
    "currentPlayer": "player-1"
  }
}
```

---

## Reporting & Monitoring

### Test Reports
- **Coverage Report:** Istanbul/NYC
- **Test Results:** Jest HTML Reporter
- **Performance Report:** Lighthouse CI
- **Security Report:** OWASP ZAP HTML Report

### Continuous Monitoring
- **Error Tracking:** Sentry
- **Performance Monitoring:** New Relic
- **Uptime Monitoring:** Pingdom
- **Contract Compliance:** Custom dashboard

---

## Success Criteria

### Test Coverage
- ✅ Unit test coverage > 80%
- ✅ Integration test coverage > 70%
- ✅ E2E test coverage > 50%
- ✅ Contract validation coverage = 100%

### Quality Gates
- ✅ All contract tests pass
- ✅ All E2E workflows complete
- ✅ Performance benchmarks met
- ✅ Security scan passes
- ✅ Accessibility audit passes
- ✅ Zero critical bugs

### Performance Benchmarks
- ✅ API p95 < 200ms
- ✅ WebSocket latency < 50ms
- ✅ Frontend FCP < 2s
- ✅ Frontend TTI < 3s

---

**Plan Version:** 1.0.0  
**Created:** 2026-06-01  
**Status:** ✅ READY FOR EXECUTION  
**Next Review:** End of Week 2