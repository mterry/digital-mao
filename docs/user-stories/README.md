# Digital Mao - User Stories & Design Artifacts

## Overview

This directory contains comprehensive user-centered design artifacts for the Digital Mao project, created following IBM Design Thinking methodology. These artifacts provide the foundation for technical contract creation and implementation.

**Project:** Digital Mao - Real-time Multiplayer Card Game with LLM Judge  
**Created:** June 2026  
**Mode:** Innovation Designer  
**Status:** ✅ Complete - Ready for Solutions Architect

---

## 📋 Table of Contents

1. [Artifacts Summary](#artifacts-summary)
2. [User Personas](#user-personas)
3. [Empathy Maps](#empathy-maps)
4. [User Stories](#user-stories)
5. [Journey Maps](#journey-maps)
6. [Key Insights](#key-insights)
7. [Design Principles](#design-principles)
8. [Next Steps](#next-steps)

---

## Artifacts Summary

### Completed Deliverables

| Artifact | File | Description | Status |
|----------|------|-------------|--------|
| **User Personas** | [`personas.md`](./personas.md) | 5 detailed personas covering all user types | ✅ Complete |
| **Empathy Maps** | [`empathy-maps.md`](./empathy-maps.md) | 4 empathy maps for key personas | ✅ Complete |
| **User Stories** | [`user-stories.md`](./user-stories.md) | 30 user stories with acceptance criteria | ✅ Complete |
| **Journey Maps** | [`journey-maps.md`](./journey-maps.md) | 3 detailed journey maps | ✅ Complete |

### Metrics

- **Total User Stories:** 30
- **Story Points:** 115 (estimated)
- **Epics:** 8
- **Personas:** 5
- **Journey Maps:** 3
- **Empathy Maps:** 4

---

## User Personas

### Primary Personas

#### 1. Sarah Chen - The Card Game Enthusiast
**Profile:** 28-year-old software developer who plays card games regularly  
**Goal:** Master complex rule systems and discover novel game mechanics  
**Pain Point:** Bored with static, predictable card games  
**Key Need:** Intellectual challenge with strategic depth

**User Stories:** US-005, US-006, US-008, US-010, US-016, US-021, US-025, US-027, US-029

---

#### 2. Marcus Rodriguez - The Mao Veteran
**Profile:** 35-year-old teacher who played Mao extensively in college  
**Goal:** Relive college gaming experiences and introduce Mao to new players  
**Pain Point:** Can't organize in-person Mao games anymore  
**Key Need:** Authentic Mao experience with natural rule creation

**User Stories:** US-002, US-004, US-017, US-018, US-019, US-020, US-022

---

#### 3. Jamie Park - The Curious Newcomer
**Profile:** 22-year-old college student learning Mao for the first time  
**Goal:** Understand the game through experience without explicit instructions  
**Pain Point:** Intimidated by steep learning curve and unclear feedback  
**Key Need:** Gentle introduction with helpful (but cryptic) guidance

**User Stories:** US-001, US-003, US-007, US-009, US-013, US-014, US-015, US-028, US-030

---

#### 4. Alex Thompson - The Rule Creator
**Profile:** 31-year-old game designer interested in emergent complexity  
**Goal:** Design creative, balanced rules that enhance gameplay  
**Pain Point:** Limited expressiveness in rule creation systems  
**Key Need:** Natural language rule input with clear compilation feedback

**User Stories:** US-017, US-018, US-019, US-020, US-023

---

#### 5. Priya Sharma - The Social Player
**Profile:** 26-year-old marketing manager who plays for social connection  
**Goal:** Have fun with friends and create memorable moments  
**Pain Point:** Toxic gaming communities and overly competitive environments  
**Key Need:** Friendly community with rich social interaction

**User Stories:** US-004, US-011, US-012, US-024, US-026

---

## Empathy Maps

Detailed empathy maps capture what users **say**, **think**, **do**, and **feel** throughout their experience:

### Key Emotional Insights

1. **Curious Newcomer (Jamie)**
   - Says: "Wait, what did I do wrong?"
   - Thinks: *I hope I don't look stupid*
   - Does: Observes carefully, takes mental notes
   - Feels: Confused → Curious → Excited → Proud

2. **Mao Veteran (Marcus)**
   - Says: "Back in college, we had this amazing rule..."
   - Thinks: *I hope this captures the spirit of physical Mao*
   - Does: Creates clever rules, provides cryptic hints
   - Feels: Nostalgic → Excited → Satisfied → Connected

3. **Rule Creator (Alex)**
   - Says: "What if we had a rule that triggers when..."
   - Thinks: *How can I create emergent complexity?*
   - Does: Analyzes patterns, tests edge cases
   - Feels: Curious → Creative → Satisfied → Proud

4. **Card Game Enthusiast (Sarah)**
   - Says: "I think I've figured out the pattern"
   - Thinks: *There's definitely a system I can learn*
   - Does: Takes notes, experiments systematically
   - Feels: Challenged → Engaged → Determined → Accomplished

**Full Details:** See [`empathy-maps.md`](./empathy-maps.md)

---

## User Stories

### Story Organization

**8 Epics covering:**
1. Game Discovery & Joining (US-001 to US-004)
2. Core Gameplay (US-005 to US-010)
3. Communication (US-011 to US-013)
4. Rule Discovery & Learning (US-014 to US-016)
5. Rule Creation (US-017 to US-020)
6. LLM Judge System (US-021 to US-023)
7. Game Management (US-024 to US-026)
8. User Experience (US-027 to US-030)

### Release Planning

#### Release 1 (MVP) - 45 Story Points
**Focus:** Core gameplay loop with basic rule creation

- US-001, US-002, US-003: Game discovery and joining
- US-005, US-006, US-007: Core gameplay mechanics
- US-009, US-010: Penalties and winning
- US-011, US-012, US-013: Basic communication
- US-017, US-018, US-019: Rule creation
- US-021: Basic judge enforcement

**Success Criteria:**
- Players can join and play games
- LLM judge enforces at least 3 custom rules
- Winners can propose and activate rules
- Chat integration functional

---

#### Release 2 (Enhanced) - 40 Story Points
**Focus:** Enhanced gameplay and management

- US-004: Lobby improvements
- US-008: Special card effects
- US-014: Penalty history
- US-022: Context-aware judgment
- US-024, US-025, US-026: Game management
- US-027: Visual feedback

**Success Criteria:**
- Special card effects working
- Context-aware judge decisions
- Robust game management
- Polished user experience

---

#### Release 3 (Complete) - 30 Story Points
**Focus:** Advanced features and polish

- US-015: Spectator mode
- US-016: Rule discovery tracking
- US-020: Rule viewing
- US-023: Judge feedback system
- US-028, US-029, US-030: UX improvements

**Success Criteria:**
- Full feature set complete
- Advanced learning tools
- Comprehensive UX polish
- Production-ready

---

### Sample User Story

**US-006: Play a Card**

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

**Full Details:** See [`user-stories.md`](./user-stories.md)

---

## Journey Maps

### Journey Map 1: New Player's First Game

**Persona:** Jamie Park (Curious Newcomer)  
**Duration:** 35 minutes  
**Emotional Arc:** Anxious → Frustrated → Curious → Excited → Satisfied

**Key Stages:**
1. **Discovery & Entry** (0-2 min) - Finding and joining game
2. **First Moments** (2-5 min) - Observing gameplay
3. **First Penalty** (5-8 min) - Learning through failure
4. **Pattern Recognition** (8-15 min) - Discovering rules
5. **Growing Confidence** (15-25 min) - Mastering basics
6. **Game Completion** (25-35 min) - Reflection and motivation

**Critical Moments:**
- First penalty (triggers learning)
- First successful play after discovery
- Watching winner create rule

**Design Implications:**
- Gentle first penalties
- Clear visual feedback
- Observation opportunities
- Progress indicators

---

### Journey Map 2: Winner Creating a Rule

**Persona:** Alex Thompson (Rule Creator)  
**Duration:** 20+ minutes  
**Emotional Arc:** Triumphant → Creative → Anxious → Satisfied → Proud

**Key Stages:**
1. **Victory & Opportunity** (0-1 min) - Earning creation privilege
2. **Rule Ideation** (1-3 min) - Designing rule concept
3. **LLM Compilation** (3-5 min) - Waiting for processing
4. **Review & Refinement** (5-8 min) - Iterating on compilation
5. **Testing & Validation** (8-10 min) - Verifying correctness
6. **Activation & Observation** (10-20 min) - Seeing rule in action
7. **Reflection & Learning** (20+ min) - Analyzing impact

**Critical Moments:**
- Winning and earning privilege
- Seeing compiled rule match intent
- First successful enforcement

**Design Implications:**
- Expressive input system
- Clear compilation feedback
- Testing capabilities
- Impact visibility

---

### Journey Map 3: Discovering a Hidden Rule

**Persona:** Sarah Chen (Card Game Enthusiast)  
**Duration:** 25+ minutes  
**Emotional Arc:** Confused → Curious → Excited → Satisfied → Confident

**Key Stages:**
1. **Initial Violation** (0-2 min) - Unexpected penalty
2. **Observation Phase** (2-8 min) - Watching others
3. **Hypothesis Testing** (8-12 min) - Experimenting
4. **Rule Refinement** (12-18 min) - Understanding nuances
5. **Pattern Generalization** (18-25 min) - Broader learning
6. **Mastery & Application** (25+ min) - Consistent success

**Critical Moments:**
- First penalty (triggers investigation)
- Observation of correct play
- Successful hypothesis test
- Mastery achievement

**Design Implications:**
- Consistent enforcement
- Pattern recognition support
- Experimentation encouragement
- Mastery indicators

**Full Details:** See [`journey-maps.md`](./journey-maps.md)

---

## Key Insights

### Cross-Persona Patterns

#### Universal Emotional Journey
```
Confusion → Frustration → Curiosity → Discovery → 
Satisfaction → Mastery → Creativity → Teaching
```

#### Common Needs
1. **Clear Feedback** - Even cryptic messages must be consistent
2. **Fair Enforcement** - AI judge must be reliable and predictable
3. **Social Connection** - Chat and community are essential
4. **Progressive Challenge** - Game must scale from beginner to expert

#### Critical Touchpoints
1. **First Penalty** - Sets tone for entire learning experience
2. **First Discovery** - Validates the learning approach
3. **First Win** - Unlocks creative participation
4. **First Rule Creation** - Transforms player into contributor

---

### Design Principles Derived from Research

#### 1. Mystery with Guidance
**Principle:** Maintain Mao's mystery while providing enough feedback to enable learning

**Implementation:**
- Cryptic but consistent penalty messages
- Visual feedback for all actions
- Pattern recognition support
- No explicit rule explanations

**User Stories:** US-009, US-013, US-014, US-021

---

#### 2. Learning Through Failure
**Principle:** Penalties are learning opportunities, not punishments

**Implementation:**
- Gentle first penalties
- Helpful (but cryptic) judge messages
- Penalty history for review
- Discovery celebration

**User Stories:** US-009, US-013, US-014, US-016

---

#### 3. Social Learning
**Principle:** Players learn from observing and interacting with others

**Implementation:**
- Rich chat system
- Spectator mode
- Visible player actions
- Community building features

**User Stories:** US-011, US-012, US-015

---

#### 4. Creative Expression
**Principle:** Winners contribute to game evolution through rule creation

**Implementation:**
- Natural language rule input
- Expressive compilation system
- Clear feedback on interpretation
- Rule testing capabilities

**User Stories:** US-017, US-018, US-019, US-020

---

#### 5. Fair Enforcement
**Principle:** AI judge must be consistent, contextual, and learnable

**Implementation:**
- Context-aware judgment
- Precedent-based decisions
- Consistent rule application
- Learning from feedback

**User Stories:** US-021, US-022, US-023

---

#### 6. Progressive Mastery
**Principle:** Clear sense of improvement from novice to expert

**Implementation:**
- Discovery tracking
- Mastery indicators
- Achievement system
- Statistics and analytics

**User Stories:** US-014, US-016, US-025

---

## Hills (User-Centric Problem Statements)

Following IBM Design Thinking methodology, we've identified these Hills:

### Hill 1: Discoverable Mystery
**Who:** New players learning Mao for the first time  
**What:** Can discover hidden rules through gameplay  
**Wow:** Without feeling frustrated or lost

**Success Metric:** 80% of new players discover at least 2 rules in their first game

**Related Stories:** US-009, US-013, US-014, US-030

---

### Hill 2: Creative Rule Making
**Who:** Winners who earn rule creation privileges  
**What:** Can express complex rule ideas in natural language  
**Wow:** And see them work exactly as intended

**Success Metric:** 90% of proposed rules compile correctly on first or second attempt

**Related Stories:** US-017, US-018, US-019, US-020

---

### Hill 3: Fair AI Judgment
**Who:** All players during gameplay  
**What:** Experience consistent, contextual rule enforcement  
**Wow:** That feels fair even when mysterious

**Success Metric:** <5% of penalties are disputed or feel unfair

**Related Stories:** US-021, US-022, US-023

---

## Technical Handoff to Solutions Architect

### Ready for Contract Creation

These user stories are ready to be translated into technical contracts:

#### OpenAPI Specifications Needed
- Game management API (US-001, US-002, US-003)
- Gameplay API (US-005, US-006, US-007, US-008)
- Chat API (US-011, US-012)
- Rule creation API (US-017, US-018, US-019)
- Judge API (US-021, US-022, US-023)

#### AsyncAPI Specifications Needed
- WebSocket events for real-time gameplay
- Game state synchronization
- Chat message streaming
- Penalty notifications
- Rule activation events

#### Component Contracts Needed
- Game board component
- Card hand component
- Chat component
- Lobby component
- Rule creation form
- Penalty notification component

#### JSON Schema Needed
- Game state model
- Player model
- Card model
- Rule model
- Penalty model
- Chat message model

---

## Story Mapping

### User Flow Priority

```
1. Join Game → 2. Play Cards → 3. Receive Penalties → 
4. Discover Rules → 5. Win Game → 6. Create Rule
```

### Feature Priority Matrix

| Feature | User Value | Technical Complexity | Priority |
|---------|-----------|---------------------|----------|
| Core Gameplay | High | Medium | P0 (MVP) |
| Chat System | High | Low | P0 (MVP) |
| Rule Creation | High | High | P0 (MVP) |
| LLM Judge | High | High | P0 (MVP) |
| Special Cards | Medium | Medium | P1 (Enhanced) |
| Penalty History | Medium | Low | P1 (Enhanced) |
| Spectator Mode | Low | Medium | P2 (Complete) |
| Discovery Tracking | Low | Medium | P2 (Complete) |

---

## Validation & Testing

### User Story Validation Checklist

All user stories have been validated against:
- ✅ Clear user value proposition
- ✅ Specific, measurable acceptance criteria
- ✅ Testable outcomes
- ✅ Appropriate story point estimation
- ✅ Dependencies identified
- ✅ Priority assigned
- ✅ Persona alignment

### Acceptance Criteria Standards

All acceptance criteria follow:
- ✅ Given-When-Then format (where applicable)
- ✅ Specific and measurable
- ✅ Include error cases
- ✅ Consider edge cases
- ✅ Specify performance requirements
- ✅ Written from user perspective

---

## Next Steps

### For Solutions Architect

1. **Review all user stories** in [`user-stories.md`](./user-stories.md)
2. **Create OpenAPI specifications** for REST endpoints
3. **Create AsyncAPI specifications** for WebSocket events
4. **Define JSON Schemas** for data models
5. **Create component contracts** for UI components
6. **Generate architectural diagrams** (C4 Model, sequence diagrams)
7. **Validate contracts** against user stories
8. **Create traceability matrix** linking contracts to stories

### For UI/UX Designer

1. **Review personas and journey maps** for design context
2. **Create wireframes** based on user stories
3. **Design component hierarchy** aligned with contracts
4. **Establish design system** for consistency
5. **Create prototypes** for key user flows
6. **Conduct accessibility audit** (WCAG 2.1 AA)

### For Development Teams

1. **Review user stories** for implementation context
2. **Wait for contracts** from Solutions Architect
3. **Implement against contracts** using TDD
4. **Validate against acceptance criteria**
5. **Conduct user testing** with personas in mind

---

## Appendix

### Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-06-01 | Innovation Designer | Initial creation of all artifacts |

### References

- [Project Requirements](../PROJECT_REQUIREMENTS.md)
- [IBM Design Thinking](https://www.ibm.com/design/thinking/)
- [User Story Best Practices](https://www.mountaingoatsoftware.com/agile/user-stories)

### Contact

For questions about these artifacts, contact the Innovation Designer mode or review the source documents.

---

## Summary Statistics

- **Total Pages:** ~2,100 lines of documentation
- **User Stories:** 30 with full acceptance criteria
- **Personas:** 5 detailed profiles
- **Journey Maps:** 3 comprehensive flows
- **Empathy Maps:** 4 detailed maps
- **Story Points:** 115 estimated
- **Epics:** 8 organized categories
- **Hills:** 3 user-centric problem statements

**Status:** ✅ Complete and ready for Solutions Architect handoff

---

*Created with IBM Design Thinking methodology*  
*Innovation Designer Mode - Digital Mao Project*  
*June 2026*