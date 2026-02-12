# NIS-2 Compliance Tool - Product Definition Document
# Product Name: "NIS2Guide Pro" (working title)
# Version: 1.0 | Date: 2026-02-12
# Status: DRAFT - Product Specification

---

## 📋 EXECUTIVE SUMMARY

### Product Vision
Create the first affordable, SMB-focused compliance tool for German companies required to comply with the NIS-2 Directive. The product will guide companies through the entire compliance journey—from scope determination to BSI registration to ongoing risk management.

### Target Market
- **Primary:** German companies with 50-250 employees in covered sectors
- **Secondary:** 50-250 employee companies in essential/important sectors
- **Tertiary:** Digital infrastructure and managed service providers (any size)

### Market Opportunity
- **~30,000 entities** now in scope (vs 4,500 previously)
- **March 6, 2026** registration deadline
- **€10M or 2% turnover** fines for non-compliance
- **No dedicated SMB tools** currently exist

### Key Value Propositions
1. **Automated scope determination** - Determine if NIS-2 applies
2. **BSI registration wizard** - Complete registration without errors
3. **Risk management templates** - Pre-built documentation
4. **Incident response playbooks** - 24-hour reporting guidance
5. **Ongoing compliance tracking** - Continuous monitoring

---

## 🎯 TARGET MARKET ANALYSIS

### Primary Customer Profiles

#### Profile 1: "The Unaware IT Manager"
**Characteristics:**
- Works at mid-sized company (50-150 employees)
- First time dealing with cybersecurity regulation
- No dedicated compliance team
- Limited budget (under €10K/year)
- Hears about NIS-2 from news or colleague

**Pain Points:**
- Doesn't know if company is in scope
- Overwhelmed by complex BSI requirements
- No time to read 100+ page regulatory documents
- Fears €10M fines but doesn't know where to start

**Needs:**
- Simple scope checker
- Step-by-step guidance
- Pre-filled templates
- Clear timeline

#### Profile 2: "The Compliance Officer"
**Characteristics:**
- Works at larger company (150-500 employees)
- Already handles GDPR, other regulations
- Has some budget (€10K-50K/year)
- Heard about NIS-2 but hasn't prioritized yet
- Receives pressure from management

**Pain Points:**
- Too many compliance tools to manage
- Needs centralized documentation
- Wants to demonstrate progress to management
- Fears audit from BSI

**Needs:**
- Integration with existing tools
- Audit-ready documentation
- Management reporting
- Board-level summaries

#### Profile 3: "The Founder/CEO"
**Characteristics:**
- Startup/scaleup (50-200 employees)
- Tech company in covered sector
- Limited compliance knowledge
- Hears about NIS-2 from advisors
- Deadline-driven

**Pain Points:**
- Wants to focus on product, not compliance
- Fines are existential threat
- Needs to show investors they're compliant
- No internal compliance resources

**Needs:**
- External expertise via tool
- Investor-ready documentation
- Clear roadmap
- Budget predictability

---

## 📊 REGULATORY REQUIREMENTS ANALYSIS

### NIS-2 Core Requirements (Article 21)

Based on the official EU NIS-2 Directive Article 21, regulated entities must implement:

#### A. Risk Analysis & Security Policies
- [ ] Policies on risk analysis and information system security
- [ ] Supply chain security policies
- [ ] Network and information systems acquisition policy
- [ ] Vulnerability handling and disclosure policy
- [ ] Assessment of cybersecurity measure effectiveness

#### B. Incident Management
- [ ] Incident handling procedures
- [ ] 24-hour initial incident notification to BSI
- [ ] 72-hour update notification
- [ ] Final report within 30 days
- [ ] Documentation of all incidents

#### C. Business Continuity
- [ ] Backup management
- [ ] Disaster recovery planning
- [ ] Crisis management procedures

#### D. Supply Chain Security
- [ ] Supplier security assessments
- [ ] Contractual security requirements
- [ ] Third-party risk management

#### E. Technical Security Measures
- [ ] Multi-factor authentication
- [ ] Access control policies
- [ ] Encryption policies
- [ ] Secure development procedures
- [ ] Asset management

#### F. Human Resources
- [ ] Cybersecurity training programs
- [ ] Access control policies
- [ ] Security awareness programs

---

## 🏗️ PRODUCT ARCHITECTURE

### Core Modules

```
┌─────────────────────────────────────────────────────────────────┐
│                    NIS2Guide Pro Platform                        │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               │
│  │  SCOPE      │ │ REGISTRATION│ │ COMPLIANCE  │               │
│  │  CHECKER    │ │  WIZARD     │ │  DASHBOARD  │               │
│  └─────────────┘ └─────────────┘ └─────────────┘               │
│                                                                 │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               │
│  │  RISK       │ │  INCIDENT   │ │  DOCUMENT   │               │
│  │  MANAGER    │ │  RESPONDER  │ │  GENERATOR │               │
│  └─────────────┘ └─────────────┘ └─────────────┘               │
│                                                                 │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               │
│  │  SUPPLY     │ │  TRAINING   │ │  REPORTING  │               │
│  │  CHAIN      │ │  ACADEMY    │ │  & EXPORT   │               │
│  └─────────────┘ └─────────────┘ └─────────────┘               │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│              Shared Services Layer                               │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐       │
│  │ Auth &    │ │ Audit     │ │ Notifi-   │ │ API       │       │
│  │ SSO       │ │ Trail     │ │ cations   │ │ Gateway   │       │
│  └───────────┘ └───────────┘ └───────────┘ └───────────┘       │
└─────────────────────────────────────────────────────────────────┘
```

### Module Descriptions

#### 1. Scope Checker
**Purpose:** Determine if company is in NIS-2 scope

**Features:**
- Sector classification wizard
- Employee count validation
- Revenue/turnover input
- Ancillary activity assessment (German-specific)
- Automatic scope determination
- PDF scope certificate generation

**Input Fields:**
- Company name and address
- Primary sector of operation
- Secondary activities
- Employee count
- Annual turnover
- Balance sheet total
- Digital infrastructure services flag

**Output:**
- "In Scope" / "Not in Scope" determination
- Classification (Essential / Important / Not Covered)
- Applicable requirements summary
- Next steps guidance

#### 2. Registration Wizard
**Purpose:** Guide users through BSI portal registration

**Features:**
- Multi-step wizard (5 steps)
- Pre-validation of inputs
- Direct Mein Unternehmenskonto (MUK) integration
- Data persistence across sessions
- Registration checklist
- Submission tracking

**Steps:**
1. **Company Information**
   - Company name, address, legal form
   - Commercial register number (Handelsregister)
   - Tax ID (Steuernummer)
   
2. **Contact Details**
   - Legal representative
   - Security officer (Sicherheitsbeauftragter)
   - Incident reporting contact
   
3. **Scope Classification**
   - Sector selection
   - Entity type (essential/important)
   - Ancillary activity declaration
   
4. **Technical Information**
   - Network infrastructure description
   - Critical services overview
   - Third-party dependencies
   
5. **Declaration & Submit**
   - Legal declaration
   - Management signature
   - BSI portal submission

#### 3. Compliance Dashboard
**Purpose:** Overview of compliance status

**Features:**
- Overall compliance score (0-100%)
- Individual requirement tracking
- Progress visualization
- Gap analysis
- Priority rankings
- Due date tracking

**Compliance Categories:**
1. Risk Management (Article 21a)
2. Incident Reporting (Article 21b)
3. Supply Chain Security (Article 21d)
4. Business Continuity (Article 21c)
5. Technical Measures (Article 21e-j)

#### 4. Risk Manager
**Purpose:** Document risk analysis and mitigation

**Features:**
- Asset inventory
- Threat identification
- Vulnerability assessment
- Risk scoring (Likelihood × Impact)
- Mitigation planning
- Residual risk documentation

#### 5. Incident Responder
**Purpose:** Guide incident reporting within 24-hour window

**Features:**
- Incident classification wizard
- Severity assessment
- 24-hour notification template
- 72-hour update wizard
- 30-day final report generator
- Evidence collection checklist

**Reporting Timeline:**
```
T0: Incident Detection
   ↓
T+1h: Initial Assessment
   ↓
T+6h: Internal Investigation
   ↓
T+24h: BSI Initial Report (mandatory)
   ↓
T+72h: Update Report (if needed)
   ↓
T+30d: Final Report
```

#### 6. Document Generator
**Purpose:** Create compliant documentation automatically

**Templates:**
- Information Security Policy
- Risk Management Framework
- Incident Response Plan
- Business Continuity Plan
- Supply Chain Security Policy
- Access Control Policy
- Training Program Records
- Management Review Minutes
- Audit Trail Reports

#### 7. Supply Chain Manager
**Purpose:** Manage third-party compliance

**Features:**
- Supplier inventory
- Critical supplier identification
- Security questionnaire automation
- Contract clause library
- Review scheduling
- Compliance verification

#### 8. Training Academy
**Purpose:** Provide required security training

**Content:**
- Management overview (2 hours)
- Staff awareness training (1 hour)
- Incident recognition (30 min)
- Secure development practices (1 hour)
- Quiz assessments
- Completion certificates

#### 9. Reporting & Export
**Purpose:** Generate compliance reports

**Reports:**
- BSI audit-ready documentation package
- Management summary
- Board-level infographic
- Gap analysis report
- Progress reports (weekly/monthly)
- Export to PDF/DOCX

---

## 👤 USER JOURNEY MAPS

### Journey A: First-Time User (The Unaware IT Manager)

```
PHASE 1: DISCOVERY (Day 0)
─────────────────────────────────────
Awareness → Search → Landing → Signup
    ↓          ↓         ↓          ↓
News/    Google    Find     Free trial → Account
Colleague "NIS-2"  tool     created
           guide

KEY TOUCHPOINTS:
• Google search: "NIS-2 Germany requirements"
• Landing page: Clear value proposition
• Free scope checker (5 questions)
• Free trial: 14 days

SUCCESS METRICS:
• Scope checker completion rate: 80%
• Trial signup after scope: 40%
─────────────────────────────────────
                    ↓
PHASE 2: EVALUATION (Days 1-7)
─────────────────────────────────────
Scope → Learn → Plan → Purchase
    ↓         ↓        ↓        ↓
In scope?  Explore   Pricing   Credit card
           features  tiers    purchase

KEY TOUCHPOINTS:
• Scope result: "Your company IS in NIS-2 scope"
• Product tour: Guided walkthrough
• Pricing page: Clear tier comparison
• ROI calculator: "Cost of compliance vs €10M fine"

VALUE DEMONSTRATION:
• Time savings: 40+ hours vs DIY
• Risk reduction: 90%+ compliance coverage
• Peace of mind: Audit-ready documentation

SUCCESS METRICS:
• Trial to paid conversion: 25%
• Average time to purchase: 3 days
─────────────────────────────────────
                    ↓
PHASE 3: ONBOARDING (Days 7-14)
─────────────────────────────────────
Welcome → Setup → First Wins → Training
    ↓         ↓         ↓          ↓
Email    Company    Compliance  Complete
Series   profile    score      training
         created    improves   module

KEY TOUCHPOINTS:
• Welcome email with quick-start guide
• Onboarding wizard (15 min setup)
• First win: Completing scope determination
• Progress celebration: Dashboard visualization

SUCCESS METRICS:
• Onboarding completion: 75%
• Training completion: 60%
─────────────────────────────────────
                    ↓
PHASE 4: ACTIVE COMPLIANCE (Days 14-60)
─────────────────────────────────────
Register → Document → Train → Monitor
    ↓         ↓          ↓          ↓
BSI      Risk mgmt  Staff       Ongoing
portal   templates  training    compliance
complete                           dashboard

KEY MILESTONES:
• Week 2: BSI registration submitted
• Week 3: Core policies generated
• Week 4: Staff training initiated
• Week 6: Risk assessment completed
• Week 8: Supply chain inventory done
• Week 10: First compliance review
─────────────────────────────────────
                    ↓
PHASE 5: ONGOING (Month 3+)
─────────────────────────────────────
Monitor → Update → Report → Renew
    ↓         ↓         ↓         ↓
Alerts    Changes   Board     Subscription
dashboard  in scope reports   renewal
          documented

KEY TOUCHPOINTS:
• Weekly compliance score updates
• Monthly management reports
• Quarterly board summaries
• Annual renewal reminder
• Ongoing regulatory updates

RETENTION DRIVERS:
• Fear of €10M fines
• BSI audit preparation
• Continuous compliance monitoring
• Annual regulatory updates
─────────────────────────────────────
```

---

## 📱 WIREFRAME DESCRIPTIONS

### Screen 1: Landing Page

```
┌─────────────────────────────────────────────────────────────────┐
│  NIS2Guide Pro                                               [Login]│
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│              NIS-2 Compliance for German Companies               │
│                                                                 │
│          The first affordable tool for mid-sized               │
│          organizations to comply with Germany's                │
│                   NIS-2 Directive                              │
│                                                                 │
│         ┌─────────────────────────────────────┐                │
│         │                                     │                │
│         │    Are you in NIS-2 scope?          │                │
│         │                                     │                │
│         │    ✓ Take the 2-minute quiz        │                │
│         │    ✓ Get your compliance roadmap    │                │
│         │    ✓ Start free trial               │                │
│         │                                     │                │
│         │         [START FREE TRIAL]           │                │
│         │                                     │                │
│         └─────────────────────────────────────┘                │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│         ⭐ Deadline: March 6, 2026      ⚠️ Fine: €10M          │
├─────────────────────────────────────────────────────────────────┤
│  Trusted by:                                                     │
│  [Company logos: 5-6 tech/consulting companies]                 │
├─────────────────────────────────────────────────────────────────┤
│  How It Works:                                                   │
│                                                                 │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐          │
│  │  Check  │→ │ Register │→ │ Document│→ │ Monitor │          │
│  │  Scope  │  │  with   │  │Compliance│  │ Ongoing │          │
│  └─────────┘  │  BSI    │  └─────────┘  └─────────┘          │
│               └─────────┘                                      │
├─────────────────────────────────────────────────────────────────┤
│  Pricing:                                                        │
│  Starter: €99/mo    Pro: €199/mo    Enterprise: €499/mo        │
│  [Compare Plans]                                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Screen 2: Compliance Dashboard

```
┌─────────────────────────────────────────────────────────────────┐
│  NIS2Guide Pro   [Company: Demo GmbH]          [Logout]        │
│  Dashboard   Registration   Compliance   Documents   Reports    │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                    COMPLIANCE OVERVIEW                      │ │
│  │                                                              │ │
│  │    ┌──────────────────────────────────────────┐            │ │
│  │    │                                          │            │ │
│  │    │          67%                            │            │ │
│  │    │                                          │            │ │
│  │    │           NIS-2 COMPLIANCE               │            │ │
│  │    │                                          │            │ │
│  │    │          [View Details →]               │            │ │
│  │    │                                          │            │ │
│  │    └──────────────────────────────────────────┘            │ │
│  │                                                              │ │
├─────────────────────────────────────────────────────────────────┤
│  NEXT DEADLINE: March 6, 2026 - BSI Registration               │
│  DAYS REMAINING: 52 days                                        │
├─────────────────────────────────────────────────────────────────┤
│  COMPLIANCE BY AREA:                                            │
│                                                                 │
│  ┌─────────────┬──────────┬────────────┬────────────────────┐   │
│  │ Area        │ Status   │ Progress   │ Action Required    │   │
│  ├─────────────┼──────────┼────────────┼────────────────────┤   │
│  │ Registration│ ⚠️ Urgent│ 10%        │ Submit BSI form   │   │
│  │ Risk Mgmt   │ ✅ On    │ 80%        │ Review risks      │   │
│  │ Training    │ ⚠️ Due   │ 40%        │ Schedule training │   │
│  │ Incidents   │ ✅ Done  │ 100%       │ —                 │   │
│  └─────────────┴──────────┴────────────┴────────────────────┘   │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  [START REGISTRATION]   [GENERATE REPORT]   [SCHEDULE DEMO]     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔄 PROCESS FLOW DIAGRAMS

### Process A: Scope Determination Flow

```
START
  │
  ▼
┌───────────────────┐
│  Sector Question  │
│  "What's your     │
│   primary sector?"│
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│  Determine Sector │
│  Classification   │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│  Size Criteria    │
│  • Employees ≥50  │
│  OR               │
│  • Revenue >€10M  │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│  Ancillary        │
│  Activity Check   │
│  (Germany-only)   │
└─────────┬─────────┘
          │
          ▼
┌───────────────┐ ┌─────────────────┐
│   IN SCOPE    │ │  NOT IN SCOPE   │
└─────────┬─────┘ └─────────┬───────┘
          │                 │
          ▼                 ▼
┌─────────────────┐ ┌─────────────────┐
│ Determine Type:  │ │  Show:          │
│ • Essential     │ │  • Why not in   │
│ • Important     │ │    scope        │
└─────────────────┘ │  • Re-check     │
                   │    in future    │
                   └─────────────────┘
          │
          ▼
   SHOW REQUIREMENTS
   & NEXT STEPS
          │
          ▼
      FINISH
```

### Process B: BSI Registration Flow

```
START REGISTRATION
       │
       ▼
┌────────────────────────────────┐
│ STEP 1: MUK Account Creation   │
│ (Mein Unternehmenskonto)        │
│ • ELSTER certificate needed    │
│ • Create account at MUK portal │
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│ STEP 2: Company Information    │
│ • Company name & address       │
│ • Legal form (Rechtsform)      │
│ • Commercial register #        │
│ • Tax ID                       │
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│ STEP 3: Contact Details        │
│ • Legal representative          │
│ • Security officer             │
│ • Incident contact             │
│ • Email & phone                │
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│ STEP 4: Scope Classification   │
│ • Sector selection             │
│ • Entity type (essential/      │
│   important)                   │
│ • Employee count               │
│ • Revenue/balance sheet        │
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│ STEP 5: Technical Details      │
│ • Network infrastructure       │
│ • Critical services           │
│ • Third-party dependencies    │
│ • Security measures           │
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│ STEP 6: Declaration           │
│ • Legal declaration          │
│ • Management signature        │
│ • Confirmation               │
└───────────────┬────────────────┘
                │
                ▼
      ┌─────────────────┐
      │ SUBMIT TO BSI   │
      │ PORTAL          │
      └─────────┬───────┘
                │
                ▼
┌────────────────────────────────┐
│ ACKNOWLEDGMENT                 │
│ • Confirmation email          │
│ • Reference number            │
│ • Submission date             │
└───────────────┬────────────────┘
                │
                ▼
      ┌─────────────────┐
      │   ONGOING:      │
      │   • Update when│
      │     changes    │
      │   • Annual    │
      │     renewal    │
      └─────────────────┘
```

---

## 💰 PRICING MODEL

### Pricing Tiers

#### Tier 1: Starter - €99/month
**Target:** Small essential/important entities (50-100 employees)

**Includes:**
- Scope determination (1 company)
- BSI registration wizard
- 5 document templates
- Basic compliance dashboard
- Email support
- 1 user seat

**Limitations:**
- 1 company only
- 5 document templates
- Email support (48h response)
- No incident responder
- No training academy
- No API access

#### Tier 2: Pro - €199/month
**Target:** Growing companies (100-250 employees)

**Includes Everything in Starter, Plus:**
- All 15 document templates
- Full compliance dashboard
- Incident response wizard
- Supply chain manager (10 suppliers)
- Training academy (3 courses)
- Priority email support (24h)
- 3 user seats
- Quarterly compliance reports

**Add-ons Available:**
- Additional users: €25/user/month
- Additional suppliers: €5/supplier/month

#### Tier 3: Enterprise - €499/month
**Target:** Larger companies (250-500 employees)

**Includes Everything in Pro, Plus:**
- Unlimited document templates
- Unlimited users
- Unlimited suppliers
- Full training academy (all courses)
- Dedicated onboarding session
- Phone support (4h response)
- API access
- Custom integrations
- White-label reports
- Multi-entity management (up to 5 entities)

**Add-ons Available:**
- Additional entities: €150/entity/month
- Dedicated support: +€200/month

### Payment Terms
- Monthly billing available
- Annual billing (2 months free = 17% discount)
- Enterprise: Annual billing only

### Free Trial
- 14-day free trial
- Full access to Starter features
- No credit card required
- Convert to paid or lose access

### Money-Back Guarantee
- 30-day money-back guarantee
- If not compliant within 90 days, refund remaining months

---

## 🚀 GO-TO-MARKET STRATEGY

### Launch Timeline

#### Phase 1: Pre-Launch (Now - March 2026)
**Goal:** Build awareness before deadline

**Activities:**
- Landing page with scope checker
- Content marketing (NIS-2 guides, webinars)
- Partnership with German business associations
- LinkedIn thought leadership
- PR in German tech publications

**Target:** 500 email signups before launch

#### Phase 2: Soft Launch (March 2026)
**Goal:** First 100 customers

**Channels:**
- Product Hunt launch
- Hacker News post
- German startup community outreach
- Compliance consultant partnerships

**Offer:** 50% off first 3 months for early adopters

**Target:** 100 paying customers

#### Phase 3: Scale (April - June 2026)
**Goal:** 500 customers

**Channels:**
- Paid advertising (Google, LinkedIn)
- Partner program (consultants, auditors)
- Content syndication
- Conference presentations

**Target:** €50K MRR

#### Phase 4: Expansion (July 2026+)
**Goal:** Expand to other EU countries

**Strategy:**
- Adapt product for other EU member states
- Partner with EU-wide compliance networks
- Enterprise sales team

**Target:** €200K MRR

### Key Messages

**For IT Managers:**
"Stop guessing. Know exactly what NIS-2 requires for your company in under 5 minutes."

**For Compliance Officers:**
"Centralize your NIS-2 compliance alongside GDPR and ISO 27001. One platform, complete visibility."

**For CEOs:**
"Your €10M fine risk, reduced. 40 hours of compliance work, automated. NIS-2 sorted."

---

## 📊 SUCCESS METRICS

### Product Metrics
- **Activation rate:** 60% of signups complete scope checker
- **Trial conversion:** 25% trial to paid
- **Feature adoption:** 80% use registration wizard
- **Retention:** 90% monthly retention after 3 months
- **NPS:** Target 50+

### Business Metrics
- **MRR target:** €50K by June 2026
- **CAC target:** <€500
- **LTV target:** >€2,000
- **Payback period:** <6 months

### Compliance Metrics
- **Registration success rate:** 95%
- **Audit pass rate:** 100%
- **Incident response time:** <24 hours

---

## 🔮 FUTURE ROADMAP

### Q2 2026
- Multi-language support (English)
- Integration with popular German ERP systems
- Mobile app for incident reporting

### Q3 2026
- Expansion to other EU member states (NIS-2 local variants)
- ISO 27001 compliance module
- SOC 2 compatibility

### Q4 2026
- AI-powered risk assessment
- Automated evidence collection
- Real-time regulatory monitoring

### 2027+
- EU AI Act compliance module
- Full GRC platform
- Market expansion (US, APAC)

---

## 📚 APPENDICES

### Appendix A: NIS-2 Sector List
Based on German implementation, covered sectors include:
1. Energy
2. Transport
3. Banking
4. Financial market infrastructure
5. Healthcare
6. Drinking water
7. Waste water
8. Digital infrastructure
9. ICT service management
10. Space
11. Public administration
12. Research

### Appendix B: Required Documentation List
1. Risk analysis policy
2. Information security policy
3. Incident response plan
4. Business continuity plan
5. Supply chain security policy
6. Access control policy
7. Training records
8. Management review minutes
9. Audit trail
10. Supplier assessments

### Appendix C: BSI Portal Links
- Mein Unternehmenskonto (MUK): https://mein-unternehmenskonto.de
- BSI NIS-2 Information: https://www.bsi.de/nis2
- Registration Portal: https://www.bsi.bund.de/nis2-registrierung

---

*Document Version: 1.0*
*Created: February 12, 2026*
*Next Review: March 1, 2026*
