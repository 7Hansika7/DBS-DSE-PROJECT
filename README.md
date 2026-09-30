# ⚡ EYE OF ODIN — 3D Campus Lost & Found Tracker

<div align="center">

![Eye of Odin Banner](https://img.shields.io/badge/Project-EYE%20OF%20ODIN-00f0ff?style=for-the-badge&logo=target&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-18+-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![Three.js](https://img.shields.io/badge/Three.js-WebGL%203D-000000?style=for-the-badge&logo=three.js&logoColor=white)
![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero%20External-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-Academic%20Open-blueviolet?style=for-the-badge)

<p align="center">
  <b>A next-generation, cyberpunk-inspired WebGL 3D item recovery platform and REST API for university campuses.</b>
  <br />
  <i>Bridging spatial telemetry, 5-vector multi-modal AI matching, anti-scam ownership validation, and security desk custody management into one cohesive interface.</i>
</p>

[Explore Documentation (PDF)](./DOCUMENTS/Project_Description_and_Output_Documentation.pdf) • [View Code](./CODE) • [Report Issue](https://github.com/7Hansika7/DBS-DSE-PROJECT/issues)

</div>

---

## 🌟 Overview & Highlights

**EYE OF ODIN** transforms the traditional lost-and-found board into a high-tech campus recovery matrix. Combining an interactive **Three.js 3D mechanical iris viewport** with a real-time **tactical HUD dock**, it enables students, faculty, and campus security to rapidly track, report, verify, and reunite lost property.

```
                  ┌────────────────────────────────────────┐
                  │          EYE OF ODIN CORE              │
                  │  3D WebGL Iris + Concentric Rune Rings │
                  └───────────────────┬────────────────────┘
                                      │
         ┌────────────────────────────┼───────────────────────────┐
         ▼                            ▼                           ▼
┌──────────────────┐        ┌──────────────────┐        ┌──────────────────┐
│  5-Vector AI     │        │  Interactive HUD │        │ Security Custody │
│  Affinity Match  │        │  Dock & Telemetry│        │ Locker Manager   │
└──────────────────┘        └──────────────────┘        └──────────────────┘
         │                            │                           │
         ▼                            ▼                           ▼
┌──────────────────┐        ┌──────────────────┐        ┌──────────────────┐
│ Anti-Scam Claim  │        │ 3D Campus Radar  │        │ Printable QR     │
│ Verification     │        │ Spatial Mapping  │        │ Poster Generator │
└──────────────────┘        └──────────────────┘        └──────────────────┘
```

---

## 📁 Repository Structure

```plaintext
DBS-DSE-PROJECT/
├── CODE/                               # Core Source Code & Deployable Bundles
│   ├── backend/                        # Zero-dependency Node.js REST API
│   │   ├── data/
│   │   │   ├── items.json              # Campus item registry persistence
│   │   │   └── claims.json             # Verification claims database
│   │   ├── package.json                # Server metadata and scripts
│   │   └── server.js                   # HTTP/REST router & static web host
│   ├── frontend/                       # Interactive WebGL 3D Client
│   │   ├── assets/logo.svg             # Vector insignia
│   │   ├── css/style.css               # Glassmorphic cyberpunk HUD layout
│   │   ├── js/
│   │   │   ├── app.js                  # Master application orchestrator
│   │   │   ├── threeScene.js           # 3D Odin mechanical eye & orbiting 3D models
│   │   │   ├── aiEngine.js             # 5-vector affinity similarity engine
│   │   │   ├── campusMap.js            # Spatial 3D campus radar & telemetry
│   │   │   ├── reportModal.js          # Multi-step lost/found wizard
│   │   │   ├── claimModal.js           # Anti-scam verification challenge
│   │   │   ├── chatController.js       # Safe campus exchange coordinator
│   │   │   ├── adminPortal.js          # Security custody locker manager
│   │   │   ├── posterGenerator.js      # Printable high-res QR recovery flyers
│   │   │   ├── aiModal.js              # Neural match breakdown visualizer
│   │   │   └── audioEngine.js          # Procedural Web Audio synthesizer
│   │   ├── index.html                  # Single-page scrollytelling interface
│   │   └── package.json                # Frontend package configuration
│   ├── backend.zip                     # Compressed backend archive
│   ├── frontend.zip                    # Compressed frontend archive
│   └── eye-of-odin-complete.zip        # Full standalone package
│
├── DOCUMENTS/                          # Formal Project Documentation & Reports
│   └── Project_Description_and_Output_Documentation.pdf
│
├── GEO TAG PICS/                       # Field Survey & Geotagged Photography
│   └── .gitkeep
│
├── CERTIFICATIONS/                     # Credentials, Badges & Verifications
│   └── .gitkeep
│
├── READ ME/                            # Auxiliary Project Guides & Manuals
│   └── README.md
│
└── README.md                           # Main Project Gateway & Documentation
```

---

## 🚀 Key Modules & Capabilities

### 1. 👁️ 3D WebGL Iris & Orbital Engine
- Built with **Three.js** featuring a dynamic cybernetic aperture, central glowing pupil, concentric rotating rune rings, and custom procedural geometry.
- Orbiting 3D interactive models representing key university items:
  - **MacBook Pro** (Electronics)
  - **AirPods Pro** (Audio Gear)
  - **Brass Keyring** (Access/Keys)
  - **Student ID Badge** (Credentials)
  - **Stainless Hydro Flask** (Personal Gear)
- Includes **Cinema View** (`👁️ Cinema View`) mode to collapse all HUD elements for an unobstructed full-screen 3D exploration.

### 2. 🧠 5-Vector Multi-Modal AI Matcher
Matches incoming lost reports with found items using a composite affinity score:
$$\text{Score} = w_c \cdot S_{\text{cat}} + w_k \cdot S_{\text{key}} + w_l \cdot S_{\text{loc}} + w_{\text{col}} \cdot S_{\text{col}} + w_t \cdot S_{\text{time}}$$

| Vector Dimension | Weight ($w$) | Metric & Algorithm |
| :--- | :---: | :--- |
| **Category Compatibility** | `30%` | Exact match & ontological parent grouping |
| **Semantic & Keywords** | `25%` | Token extraction + Jaccard similarity coefficient |
| **Spatial Proximity** | `20%` | Euclidean distance across 3D campus coordinates |
| **Color Affinity** | `15%` | Hex color distance & naming token cross-check |
| **Temporal Proximity** | `10%` | Exponential decay over days since incident |

### 3. 🛡️ Anti-Scam Claim Verification Protocol
- Solves the common campus vulnerability of fraudulent claims.
- Finders can attach **Secret Verification Challenges** (e.g., *"What sticker is on the back cover?"* or *"What are the last 4 digits of the serial number?"*).
- Claimants must satisfy the security criteria before contact details or exchange locations are revealed.

### 4. 🏢 Security Desk Custody Locker Manager
- Track items physically secured in campus safety vaults (`Locker A-04`, `Locker B-12`, `Locker C-09`).
- Status logging, chain-of-custody tracking, and verified student ID handover.

### 5. 🖨️ Printable QR Poster Generator
- In-browser SVG/Canvas engine producing ready-to-print flyers formatted for standard campus bulletin boards.
- Embedded QR code directs finders straight to the active claim verification portal.

---

## ⚡ Quick Start Guide

### Prerequisites
- **Node.js** (v16.0 or higher recommended)
- Any modern web browser supporting WebGL (Chrome, Edge, Firefox, Safari)

### Option 1: Standalone Integrated Node Server (Recommended)
The server runs zero external npm packages and simultaneously serves the API and static 3D frontend:

```bash
# 1. Clone repository
git clone https://github.com/7Hansika7/DBS-DSE-PROJECT.git
cd DBS-DSE-PROJECT/CODE/backend

# 2. Launch server (zero dependencies required)
node server.js
```

Open your browser and navigate to:
👉 **`http://localhost:5050`**

### Option 2: Live Server (Frontend Only)
1. Open the repository in **VS Code**.
2. Right-click on [`CODE/frontend/index.html`](./CODE/frontend/index.html).
3. Select **"Open with Live Server"**.
4. *(Optional)* Run `node CODE/backend/server.js` to enable live persistence with REST endpoints.

---

## 📡 REST API Reference

| Endpoint | Method | Description | Parameters / Payload |
| :--- | :---: | :--- | :--- |
| `/api/health` | `GET` | System heartbeat & server uptime | None |
| `/api/stats` | `GET` | Campus analytics & recovery KPIs | `totalLost`, `totalFound`, `reunionRate` |
| `/api/items` | `GET` | Retrieve and filter campus items | `?type=`, `?category=`, `?priority=`, `?q=` |
| `/api/items` | `POST` | Register a new lost or found item | JSON item specification |
| `/api/items/:id` | `PATCH` | Update status, custody, or details | Partial JSON update object |
| `/api/claims` | `GET` | List ownership claims | Filterable by `itemId` or `status` |
| `/api/claims` | `POST` | Submit verification challenge response | Claimant details & secret answer |
| `/api/items/match/:id` | `GET` | AI match ranking for a specific item | Returns top matches with score breakdown |

---

## 📊 Priority Classification

- 🔴 **Critical Priority**: Academic thesis laptops, national passports, prescription medications, high-security access cards.
- 🟡 **High Urgency**: Smartphones, vehicle key sets, wallets, student transit cards.
- 🔵 **Standard Urgency**: Water bottles, outerwear, umbrellas, textbooks, stationery.

---

## 📄 Documentation & PDF Report

A comprehensive, publication-styled PDF report containing the **complete project architecture, system methodology, output description, and UI walkthrough** is available in the [`DOCUMENTS/`](./DOCUMENTS) directory:

👉 **[Download Project Description & Output PDF](./DOCUMENTS/Project_Description_and_Output_Documentation.pdf)**

---

<div align="center">
  <sub>Engineered with precision for university campus safety and lost-and-found efficiency.</sub>
</div>
