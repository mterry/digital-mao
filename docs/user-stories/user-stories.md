# User Stories - Digital Mao

## Epic 1: Game Discovery & Joining

### US-001: Browse Available Games
**As a** Card Game Enthusiast  
**I want to** see a list of available games to join  
**So that** I can find a game that matches my preferences

**Acceptance Criteria:**
- [ ] Display shows all open games waiting for players
- [ ] Each game listing shows: number of players (current/max), game status, host name
- [ ] Games are sorted by creation time (newest first)
- [ ] List updates in real-time as games are created/filled
- [ ] User can filter games by player count
- [ ] Empty state message shown when no games available
- [ ] Loading state shown while fetching games

**Story Points:** 3  
**Priority:** High  
**Dependencies:** None

---

### US-002: Create New Game
**As a** Mao Veteran  
**I want to** create a new game with specific settings  
**So that** I can host a game for my friends

**Acceptance Criteria:**
- [ ] User can set maximum player count (2-8)
- [ ] User can set game name/title
- [ ] User can choose to make game private (invite-only)
- [ ] Game is created and user becomes host
- [ ] User is automatically placed in game lobby
- [ ] Game appears in available games list (if public)
- [ ] Unique game ID/code generated for sharing
- [ ] Validation prevents invalid settings

**Story Points:** 3  
**Priority:** High  
**Dependencies:** None

---

### US-003: Join Existing Game
**As a** Curious Newcomer  
**I want to** join an existing game  
**So that** I can start playing quickly

**Acceptance Criteria:**
- [ ] User can click on game from list to join
- [ ] User can enter game code to join private game
- [ ] System validates game is not full before joining
- [ ] User is added to game lobby immediately
- [ ] All players in lobby see new player join
- [ ] Error message shown if game is full or invalid
- [ ] User can leave lobby before game starts

**Story Points:** 2  
**Priority:** High  
**Dependencies:** US-001, US-002

---

### US-004: Wait in Game Lobby
**As a** Social Player  
**I want to** see who else is in the lobby and chat before game starts  
**So that** I can socialize and prepare for the game

**Acceptance Criteria:**
- [ ] Lobby shows all joined players with names
- [ ] Chat is available in lobby
- [ ] Host can start game when 2+ players present
- [ ] Host can kick players from lobby
- [ ] Players can mark themselves as "ready"
- [ ] Countdown shown when host starts game
- [ ] Players can leave lobby voluntarily
- [ ] Game auto-starts when lobby is full (8 players)

**Story Points:** 3  
**Priority:** Medium  
**Dependencies:** US-003

---

## Epic 2: Core Gameplay

### US-005: View Game State
**As a** Card Game Enthusiast  
**I want to** see the current game state clearly  
**So that** I can make informed decisions

**Acceptance Criteria:**
- [ ] My hand of cards is displayed clearly
- [ ] Current player's turn is highlighted
- [ ] Discard pile shows top card
- [ ] Draw pile shows card count
- [ ] All players' card counts are visible
- [ ] Turn direction indicator is shown
- [ ] Current suit (if changed by 8) is displayed
- [ ] Game state updates in real-time (<100ms)
- [ ] Visual feedback for all state changes

**Story Points:** 5  
**Priority:** High  
**Dependencies:** US-003

---

### US-006: Play a Card
**As a** Card Game Enthusiast  
**I want to** play a card from my hand  
**So that** I can progress the game

**Acceptance Criteria:**
- [ ] User can click/tap card to select it
- [ ] Selected card is highlighted
- [ ] "Play Card" button is enabled when card selected
- [ ] Card is played when button clicked
- [ ] Card moves from hand to discard pile with animation
- [ ] Turn advances to next player automatically
- [ ] Invalid plays are rejected with visual feedback
- [ ] Card count updates immediately
- [ ] Other players see card played in real-time

**Story Points:** 5  
**Priority:** High  
**Dependencies:** US-005

---

### US-007: Draw a Card
**As a** Curious Newcomer  
**I want to** draw a card when I can't play  
**So that** I can continue participating

**Acceptance Criteria:**
- [ ] "Draw Card" button is available on my turn
- [ ] Card is drawn from deck when button clicked
- [ ] New card appears in my hand with animation
- [ ] Draw pile count decrements
- [ ] Turn advances to next player
- [ ] If deck is empty, discard pile is shuffled into deck
- [ ] Other players see that I drew a card
- [ ] System prevents drawing when I have playable cards (if rule active)

**Story Points:** 3  
**Priority:** High  
**Dependencies:** US-005

---

### US-008: Handle Special Card Effects
**As a** Card Game Enthusiast  
**I want to** see special card effects take place  
**So that** the game has strategic depth

**Acceptance Criteria:**
- [ ] Playing an 8 prompts suit selection
- [ ] Selected suit is displayed to all players
- [ ] Playing an Ace reverses turn direction
- [ ] Direction indicator updates immediately
- [ ] Playing a Queen skips next player
- [ ] Skipped player is visually indicated
- [ ] All special effects are animated
- [ ] Effects are applied before turn advances
- [ ] Other players see effects in real-time

**Story Points:** 5  
**Priority:** Medium  
**Dependencies:** US-006

---

### US-009: Receive Penalty
**As a** Curious Newcomer  
**I want to** be notified when I break a rule  
**So that** I can learn from my mistakes

**Acceptance Criteria:**
- [ ] Penalty notification appears immediately
- [ ] Message is cryptic but hints at the violation
- [ ] Penalty cards are added to my hand
- [ ] Card count updates to reflect penalty
- [ ] Penalty is logged in game history
- [ ] Other players see that I was penalized
- [ ] Penalty message is stored for later review
- [ ] Visual/audio feedback indicates penalty

**Story Points:** 3  
**Priority:** High  
**Dependencies:** US-006

---

### US-010: Win a Round
**As a** Card Game Enthusiast  
**I want to** be recognized when I empty my hand  
**So that** I can earn rule creation privileges

**Acceptance Criteria:**
- [ ] Game detects when player has zero cards
- [ ] Winner announcement is displayed to all players
- [ ] Winner is given option to propose new rule
- [ ] Game state is frozen until rule is proposed/declined
- [ ] Winner's name is highlighted
- [ ] Celebration animation is shown
- [ ] Game statistics are updated
- [ ] Option to start new round is presented

**Story Points:** 3  
**Priority:** High  
**Dependencies:** US-006

---

## Epic 3: Communication

### US-011: Send Chat Message
**As a** Social Player  
**I want to** send messages to other players  
**So that** I can communicate during the game

**Acceptance Criteria:**
- [ ] Chat input field is always accessible
- [ ] User can type and send messages
- [ ] Messages appear in chat history immediately
- [ ] User's name is shown with each message
- [ ] Timestamp is displayed for each message
- [ ] Chat scrolls to show latest messages
- [ ] Enter key sends message
- [ ] Empty messages are not sent
- [ ] Messages are limited to 500 characters

**Story Points:** 2  
**Priority:** High  
**Dependencies:** US-005

---

### US-012: Receive Chat Messages
**As a** Social Player  
**I want to** see messages from other players  
**So that** I can follow the conversation

**Acceptance Criteria:**
- [ ] Messages from other players appear in real-time
- [ ] Each message shows sender name and timestamp
- [ ] Messages are displayed in chronological order
- [ ] Chat history is preserved during game
- [ ] System messages are visually distinct
- [ ] Judge messages are highlighted differently
- [ ] Chat auto-scrolls to new messages
- [ ] User can scroll up to see history

**Story Points:** 2  
**Priority:** High  
**Dependencies:** US-011

---

### US-013: Receive Judge Feedback
**As a** Curious Newcomer  
**I want to** receive cryptic hints from the judge  
**So that** I can learn rules without explicit explanations

**Acceptance Criteria:**
- [ ] Judge messages appear in chat
- [ ] Judge messages are visually distinct (different color/icon)
- [ ] Messages are cryptic but provide clues
- [ ] Messages reference the specific violation
- [ ] Messages maintain Mao's mystery
- [ ] Messages are stored in game history
- [ ] User can review past judge messages
- [ ] Messages are contextual to the situation

**Story Points:** 3  
**Priority:** High  
**Dependencies:** US-012

---

## Epic 4: Rule Discovery & Learning

### US-014: View Penalty History
**As a** Card Game Enthusiast  
**I want to** review my past penalties  
**So that** I can identify patterns and learn rules

**Acceptance Criteria:**
- [ ] User can access penalty history panel
- [ ] All penalties are listed chronologically
- [ ] Each entry shows: timestamp, action taken, penalty received
- [ ] Judge's message is displayed for each penalty
- [ ] User can filter by penalty type
- [ ] History persists across game sessions
- [ ] User can export history for analysis
- [ ] Clear visual design for easy scanning

**Story Points:** 3  
**Priority:** Medium  
**Dependencies:** US-009

---

### US-015: Observe Game as Spectator
**As a** Curious Newcomer  
**I want to** watch a game without playing  
**So that** I can learn before joining

**Acceptance Criteria:**
- [ ] User can join game as spectator
- [ ] Spectator sees all public game state
- [ ] Spectator cannot see players' hands
- [ ] Spectator can see chat messages
- [ ] Spectator can send chat messages
- [ ] Spectator messages are marked as from spectator
- [ ] Spectator can leave at any time
- [ ] Spectator count is displayed to players

**Story Points:** 3  
**Priority:** Low  
**Dependencies:** US-005

---

### US-016: Track Rule Discovery Progress
**As a** Card Game Enthusiast  
**I want to** see which rules I've discovered  
**So that** I can track my learning progress

**Acceptance Criteria:**
- [ ] User has access to "discovered rules" panel
- [ ] Rules are marked as discovered after consistent compliance
- [ ] Each rule shows discovery date
- [ ] Rules are categorized by type
- [ ] Progress indicator shows % of rules discovered
- [ ] User can mark rules as "understood"
- [ ] Hints are provided for undiscovered rules
- [ ] Achievement system for discovering all rules

**Story Points:** 5  
**Priority:** Low  
**Dependencies:** US-009

---

## Epic 5: Rule Creation

### US-017: Propose New Rule
**As a** Rule Creator  
**I want to** propose a new rule in natural language  
**So that** I can add complexity to the game

**Acceptance Criteria:**
- [ ] Winner is prompted to propose rule
- [ ] Text input accepts natural language description
- [ ] User can provide detailed rule explanation
- [ ] User can specify rule priority/category
- [ ] User can decline to add rule
- [ ] Rule is sent to LLM for compilation
- [ ] Loading indicator shown during compilation
- [ ] Character limit is enforced (1000 chars)

**Story Points:** 3  
**Priority:** High  
**Dependencies:** US-010

---

### US-018: Review Compiled Rule
**As a** Rule Creator  
**I want to** see how my rule was interpreted  
**So that** I can confirm it matches my intent

**Acceptance Criteria:**
- [ ] Compiled rule is displayed to creator
- [ ] Rule shows: trigger conditions, actions, penalties
- [ ] Creator can approve or reject compilation
- [ ] Creator can provide feedback if rejected
- [ ] Creator can edit original description
- [ ] System shows potential conflicts with existing rules
- [ ] Examples of rule application are shown
- [ ] Creator can test rule against scenarios

**Story Points:** 5  
**Priority:** High  
**Dependencies:** US-017

---

### US-019: Activate New Rule
**As a** Rule Creator  
**I want to** activate my approved rule  
**So that** it becomes part of the game

**Acceptance Criteria:**
- [ ] Rule is added to active rules list
- [ ] All players are notified of new rule (cryptically)
- [ ] Rule takes effect immediately
- [ ] Rule is stored in database
- [ ] Rule is assigned unique identifier
- [ ] Rule priority is set correctly
- [ ] Judge begins enforcing rule
- [ ] Rule appears in game's rule history

**Story Points:** 3  
**Priority:** High  
**Dependencies:** US-018

---

### US-020: View Active Rules (Creator Only)
**As a** Rule Creator  
**I want to** see all active rules and their details  
**So that** I can understand the current rule set

**Acceptance Criteria:**
- [ ] Creator can access rules panel
- [ ] All active rules are listed
- [ ] Each rule shows: description, creator, activation date
- [ ] Rules are sorted by priority
- [ ] Creator can see enforcement statistics
- [ ] Creator can see rule interactions
- [ ] Visual indicators for rule conflicts
- [ ] Export functionality for rule set

**Story Points:** 3  
**Priority:** Medium  
**Dependencies:** US-019

---

## Epic 6: LLM Judge System

### US-021: Automatic Rule Enforcement
**As a** Card Game Enthusiast  
**I want to** have rules enforced consistently  
**So that** the game is fair

**Acceptance Criteria:**
- [ ] Judge evaluates every game action
- [ ] Violations are detected within 2 seconds
- [ ] Penalties are applied automatically
- [ ] Judge considers game context (recent history)
- [ ] Judge handles multiple simultaneous violations
- [ ] Judge respects rule priority for conflicts
- [ ] Judge provides cryptic feedback
- [ ] Enforcement is logged for analysis

**Story Points:** 8  
**Priority:** High  
**Dependencies:** US-006, US-019

---

### US-022: Context-Aware Judgment
**As a** Mao Veteran  
**I want to** the judge to consider game context  
**So that** enforcement is intelligent and fair

**Acceptance Criteria:**
- [ ] Judge analyzes last 10 game actions
- [ ] Judge considers player history
- [ ] Judge identifies repeated violations
- [ ] Judge adjusts penalties for context
- [ ] Judge recognizes edge cases
- [ ] Judge uses precedents for consistency
- [ ] Judge explains reasoning (in logs, not to players)
- [ ] Judge learns from creator feedback

**Story Points:** 8  
**Priority:** Medium  
**Dependencies:** US-021

---

### US-023: Handle Ambiguous Situations
**As a** Rule Creator  
**I want to** provide feedback on ambiguous judgments  
**So that** the judge improves over time

**Acceptance Criteria:**
- [ ] Creator can flag judgments as incorrect
- [ ] Creator can provide correct interpretation
- [ ] Feedback is stored in knowledge graph
- [ ] Judge uses feedback for future similar cases
- [ ] Creator sees acknowledgment of feedback
- [ ] Feedback is reviewed by system
- [ ] Patterns in feedback are identified
- [ ] Judge accuracy improves over time

**Story Points:** 5  
**Priority:** Low  
**Dependencies:** US-021

---

## Epic 7: Game Management

### US-024: Handle Player Disconnection
**As a** Social Player  
**I want to** the game to continue if someone disconnects  
**So that** one player's connection issues don't ruin the game

**Acceptance Criteria:**
- [ ] Disconnected player is marked as "disconnected"
- [ ] Game continues with remaining players
- [ ] Disconnected player's turn is skipped
- [ ] Player can reconnect within 5 minutes
- [ ] Reconnected player resumes with same hand
- [ ] If player doesn't reconnect, they are removed
- [ ] Other players are notified of disconnection
- [ ] Game ends if too few players remain

**Story Points:** 5  
**Priority:** High  
**Dependencies:** US-005

---

### US-025: End Game
**As a** Card Game Enthusiast  
**I want to** see game results when it ends  
**So that** I can review performance

**Acceptance Criteria:**
- [ ] Game ends when winner is declared
- [ ] Final standings are displayed
- [ ] Statistics are shown: penalties, cards played, etc.
- [ ] Players can start new game with same group
- [ ] Players can return to lobby
- [ ] Game history is saved
- [ ] Players can export game summary
- [ ] Option to rematch is provided

**Story Points:** 3  
**Priority:** Medium  
**Dependencies:** US-010

---

### US-026: Leave Game Early
**As a** Social Player  
**I want to** leave a game if needed  
**So that** I'm not forced to stay

**Acceptance Criteria:**
- [ ] User can click "Leave Game" button
- [ ] Confirmation dialog is shown
- [ ] User is removed from game immediately
- [ ] Other players are notified
- [ ] User's cards are removed from game
- [ ] Game continues with remaining players
- [ ] User can join other games
- [ ] Leaving is logged in game history

**Story Points:** 2  
**Priority:** Medium  
**Dependencies:** US-005

---

## Epic 8: User Experience

### US-027: Receive Visual Feedback
**As a** Curious Newcomer  
**I want to** see clear visual feedback for all actions  
**So that** I understand what's happening

**Acceptance Criteria:**
- [ ] Card plays are animated
- [ ] Turn changes are highlighted
- [ ] Penalties show visual effect
- [ ] Valid/invalid actions have distinct feedback
- [ ] Loading states are shown
- [ ] Success/error messages are clear
- [ ] Hover states indicate interactivity
- [ ] Animations are smooth (60fps)

**Story Points:** 5  
**Priority:** Medium  
**Dependencies:** US-006

---

### US-028: Access Help System
**As a** Curious Newcomer  
**I want to** access help without breaking the mystery  
**So that** I can get oriented without spoiling the game

**Acceptance Criteria:**
- [ ] Help button is always accessible
- [ ] Help explains basic mechanics only
- [ ] Help does not reveal hidden rules
- [ ] Help includes UI navigation guide
- [ ] Help shows keyboard shortcuts
- [ ] Help can be dismissed easily
- [ ] Help is contextual to current screen
- [ ] Help includes FAQ section

**Story Points:** 3  
**Priority:** Low  
**Dependencies:** None

---

### US-029: Customize Settings
**As a** Card Game Enthusiast  
**I want to** customize my experience  
**So that** the game suits my preferences

**Acceptance Criteria:**
- [ ] User can adjust sound volume
- [ ] User can toggle animations
- [ ] User can change card design
- [ ] User can adjust chat font size
- [ ] User can enable/disable notifications
- [ ] Settings persist across sessions
- [ ] Settings sync across devices
- [ ] Default settings are sensible

**Story Points:** 3  
**Priority:** Low  
**Dependencies:** None

---

### US-030: View Game Tutorial
**As a** Curious Newcomer  
**I want to** complete an interactive tutorial  
**So that** I understand basic mechanics before playing

**Acceptance Criteria:**
- [ ] Tutorial is offered to new users
- [ ] Tutorial covers basic card playing
- [ ] Tutorial explains turn structure
- [ ] Tutorial demonstrates chat usage
- [ ] Tutorial can be skipped
- [ ] Tutorial can be replayed later
- [ ] Tutorial does not reveal hidden rules
- [ ] Tutorial takes less than 5 minutes

**Story Points:** 5  
**Priority:** Medium  
**Dependencies:** US-005

---

## Story Map Summary

### Release 1 (MVP)
- US-001, US-002, US-003: Game discovery and joining
- US-005, US-006, US-007: Core gameplay
- US-009, US-010: Penalties and winning
- US-011, US-012, US-013: Basic communication
- US-017, US-018, US-019: Rule creation
- US-021: Basic judge enforcement

### Release 2 (Enhanced)
- US-004: Lobby improvements
- US-008: Special card effects
- US-014: Penalty history
- US-022: Context-aware judgment
- US-024, US-025, US-026: Game management
- US-027: Visual feedback

### Release 3 (Complete)
- US-015: Spectator mode
- US-016: Rule discovery tracking
- US-020: Rule viewing
- US-023: Judge feedback
- US-028, US-029, US-030: UX improvements

---

## Acceptance Criteria Guidelines

All user stories follow these standards:
- Criteria are specific and measurable
- Criteria are testable (can be verified)
- Criteria define "done" clearly
- Criteria include error cases
- Criteria consider edge cases
- Criteria specify performance requirements where relevant
- Criteria are written from user perspective

## Story Point Scale
- 1-2 points: Simple, well-understood tasks
- 3 points: Moderate complexity, some unknowns
- 5 points: Complex, multiple components
- 8 points: Very complex, significant unknowns
- 13+ points: Epic, should be broken down

## Priority Definitions
- **High:** Must have for MVP
- **Medium:** Important for full release
- **Low:** Nice to have, can be deferred