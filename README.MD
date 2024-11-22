[English](README.ew.md)
# 스페이스 엔지니어 SEK 서버

## 개요

스페이스 엔지니어 SEK 서버에 오신 것을 환영합니다!  
이 서버는 네 개의 주요 서버로 구성되어 있으며, 각각의 서버는 고유한 특성을 가지고 있습니다:

1. **SEK_General**
2. **SEK_Safe Boundary**
3. **SEK_CORE**
4. **SEK_Vanguard Realm**

## 서버 상세 정보

### **SEK_General**
- **좌표**: 0,0,0  
- **범위**: 반경 200000km  
- **PCU제한**: 서버 상태나 활성 유저수에 따라 서버장이 유동적으로 조정합니다(현재 4.5만). 
  - 전체 월드를 아우르는 서버입니다.  
  - 나머지 서버가 이 서버 내부에 포함되어 있습니다.  
  - 서버 재시작 시 지형이 초기화.

### **SEK_Safe Boundary**
- **좌표**: 0,0,0  
- **범위**: 반경 500km  
- **PCU제한**: 서버 상태나 활성 유저수에 따라 서버장이 유동적으로 조정합니다(현재 20만). 
  - EarthLike 행성과 달이 포함된 안정적인 입문용 서버입니다.  
  - 지형 초기화가 없습니다.  
  - 랜덤 인카운터 옵션이 꺼져 있습니다.

### **SEK_CORE**
- **좌표**: -3967231.5, -32231.5, -767231.5  
- **범위**: 반경 300km  
- **PCU 제한**: 18000  
  - 서버에 진입하면서 PCU제한을 넘기게 되는 경우 해당 서버에서 접속이 끊기면 그리드가 삭제됩니다. 이런 경우로 발생한 손실은 절대 복구해드리지 않습니다. 
  - Pertam 행성을 중심으로 한 서버입니다.  
  - 다양한 모드의 NPC 함선이 존재하며, 유저가 NPC에게 입힌 데미지를 기반으로 점수가 기록됩니다.  
  - 점수는 별도의 DB에 저장되며, 웹 사이트에서 확인할 수 있습니다.  
  - NPC와의 전투 시 온라인 인벤토리에 아이템이 드랍됩니다. 특수 모듈은 현재 이 방법으로만 획득할 수 있습니다.  
  - 온라인 인벤토리에 드랍된 아이템은 다른 서버에서도 다운로드가 가능합니다. 이 서버는 귀환 및 그리드 수거 부담 없이 전투를 즐기는게 가능하게 설계되었습니다.  
  - 서버 재시작 시 지형이 초기화.

### **SEK_Vanguard Realm**
- **좌표**: 131072.50, 131072.50, 5731072.50  
- **범위**: 반경 1000km  
- **PCU제한**: 서버 상태나 활성 유저수에 따라 서버장이 유동적으로 조정합니다(현재 6만). 
- **자원 배율**: 우라늄/백금/은/금 배율 높음  
- **특징**: 유저가 건설 불가능한 특수 무기블럭으로 강화된 NPC 출몰  
- 서버 재시작 시 지형이 초기화.

## 공통 특징

- **쉴드 시스템**: 플레이어와 구조물을 보호하는 방어 쉴드를 제공합니다.
- **업그레이드 모듈**: 공격/방어/스러스터 효율을 증가시키는 모듈로, 최대 10레벨까지 업그레이드 가능합니다. NPC 그리드에도 적용되며, 그리드 이름에 모듈 레벨의 총합이 표시됩니다. 모듈은 콕핏 이름에 `[Upgrade]`를 포함시키고, 해당 블록의 인벤토리에 모듈을 넣어 적용됩니다.


## 서버 규칙

- **서버 관련 문의**: 서버 운영자를 부르기 전에 [도움말](https://github.com/snowmuffin/SEK_Server/wiki/%EC%9C%A0%EC%A0%80-%EB%AA%85%EB%A0%B9%EC%96%B4)을 확인해 주세요.
- **NPC 그리드 재활용**: NPC 그리드를 이름 변경 없이 재활용하거나 소유권을 완전히 얻지 않은 상태로 사용할 경우 문제가 발생할 수 있습니다.
- **인게임 이름**: 팩션, 블록, 그리드, 유저명 등에 한글 이름을 사용할 경우 문제가 생길 수 있으므로, 가급적 영어 이름을 사용해 주세요.
- **PVP 규칙**:  PVP제한은 따로 없습니다. 자유롭게 싸우시면 됩니다.
- **건설 제한**: 서버 환경에 부정적인 영향을 미칠 수 있는 요소는 제한될 수 있습니다.
- **서버 안정성 보호**: 무분별한 대규모 구조물 건설, 스크립트 남용, 아이템 스팸 등을 자제해 주세요. 이는 모든 플레이어의 원활한 게임플레이를 위해 필요합니다.

## 디스코드

서버 관련 문의 및 커뮤니티 소통을 위해 디스코드에 참여해 주세요:  
[디스코드 링크](https://discord.gg/WJqeXfv6M9)  
[서버 로드맵](https://successful-airboat-f57.notion.site/10575e0bd20580e5b476dd6cb2dcd47e?v=3955b1d0efc74980b8cb51a306cbaf71)

# SEK_Server 기여자

- **Nicola**  
  SEK_SERVER의 웹 컨텐츠는 Nicola님이 제공해 주신 프론트엔드를 사용했습니다. 그 외에도 디코 편의성 개선을 위한 봇을 제작 해주셨습니다.

- **Nya-Nya-Nyang**  
  Upgrade_module 모드의 아이콘을 제공해 주셨습니다.

- **RaDDo**  
  각종 테스트 및 버그 발견을 포함하여 여러 부분에서 도움을 주셨습니다.

- **붕붕(op206)**  
  서버 초기부터 함께하며 여러 조언 및 관리 아이디어를 제공해 주셨고, 홍보에도 힘써 주셨습니다.

- **Arstraea**  
  게임의 이해도가 높아 여러 피드백과 문제 해결 방법을 제시해 주셨습니다.

- **SGL**  
  정말 멋진 서버 아이콘을 제작해 주셨습니다.

---

이 외에도 서버에 다양한 방식으로 참여해 주신 모든 분들께 진심으로 감사드립니다.



# Space Engineers SEK Server

## Overview

Welcome to the Space Engineers SEK Server!

This server consists of four main servers, each with its own unique characteristics:

1. **SEK_General**
2. **SEK_Safe Boundary**
3. **SEK_CORE**
4. **SEK_Vanguard Realm**

## Server Details

### **SEK_General**
- **Coordinates**: 0,0,0  
- **Range**: Radius of 200,000 km  
- **PCU Limit**: Adjusted flexibly by the server owner based on server status and active user count (currently 45,000). 
  - This server encompasses the entire world.  
  - The other servers are included within this server.  
  - Terrain resets upon server restart.

### **SEK_Safe Boundary**
- **Coordinates**: 0,0,0  
- **Range**: Radius of 500 km  
- **PCU Limit**: Adjusted flexibly by the server owner based on server status and active user count (currently 200,000). 
  - A stable beginner server that includes EarthLike planet and moon.  
  - No terrain resets.  
  - Random encounter option is turned off.

### **SEK_CORE**
- **Coordinates**: -3,967,231.5, -32,231.5, -767,231.5  
- **Range**: Radius of 300 km  
- **PCU Limit**: 18,000  
  - If you exceed the PCU limit upon entering the server, your grid will be deleted when you disconnect. Losses incurred in such cases will not be restored under any circumstances. 
  - A server centered around the Pertam planet.  
  - Various modded NPC ships exist, and scores are recorded based on the damage players inflict on NPCs.  
  - Scores are saved in a separate database and can be viewed on the website.  
  - Items drop into the online inventory when battling NPCs. Special modules can only be obtained this way currently.  
  - Items dropped into the online inventory can be downloaded on other servers. This server is designed to allow players to enjoy combat without the burden of returning or collecting grids.  
  - Terrain resets upon server restart.

### **SEK_Vanguard Realm**
- **Coordinates**: 131,072.50, 131,072.50, 5,731,072.50  
- **Range**: Radius of 1,000 km  
- **PCU Limit**: Adjusted flexibly by the server owner based on server status and active user count (currently 60,000). 
- **Resource Multiplier**: High multiplier for Uranium/Platinum/Silver/Gold  
- **Features**: Appearance of NPCs reinforced with special weapon blocks that players cannot construct  
- Terrain resets upon server restart.

## Common Features

- **Shield System**: Provides defensive shields to protect players and structures.
- **Upgrade Modules**: Modules that increase attack/defense/thruster efficiency, upgradable up to level 10. They also apply to NPC grids, and the total module level is displayed in the grid's name. To apply a module, include `[Upgrade]` in the cockpit's name and place the module in the inventory of that block.

## Server Rules

- **Server Inquiries**: Please check the [Help Guide](https://github.com/snowmuffin/SEK_Server/wiki/%EC%9C%A0%EC%A0%80-%EB%AA%85%EB%A0%B9%EC%96%B4) before contacting the server administrator.
- **Recycling NPC Grids**: Issues may arise if you recycle NPC grids without changing their names or use them without fully acquiring ownership.
- **In-game Names**: Problems may occur when using Korean names for factions, blocks, grids, or usernames. Please use English names whenever possible.
- **PVP Rules**: There are no specific PVP restrictions. Feel free to engage in combat.
- **Construction Restrictions**: Elements that may negatively affect the server environment may be restricted.
- **Server Stability Protection**: Please refrain from reckless construction of large structures, overuse of scripts, or item spamming. This is necessary for smooth gameplay for all players.

## Discord

Please join our Discord for server inquiries and community interaction:  
[Discord Link](https://discord.gg/WJqeXfv6M9)  
[Server Roadmap](https://successful-airboat-f57.notion.site/10575e0bd20580e5b476dd6cb2dcd47e?v=3955b1d0efc74980b8cb51a306cbaf71)

# SEK_Server Contributors

- **Nicola**  
  The web content of SEK_SERVER uses the frontend provided by Nicola. Additionally, they have developed bots to improve Discord convenience.

- **Nya-Nya-Nyang**  
  Provided icons for the Upgrade_module mod.

- **RaDDo**  
  Assisted in various areas including testing and bug discovery.

- **붕붕(op206)**  
  Has been with us since the early days of the server, providing various advice and management ideas, and has also helped with promotion.

- **Arstraea**  
  With a high understanding of the game, has provided various feedback and solutions to problems.

- **SGL**  
  Created a really cool server icon.

---

We sincerely thank everyone else who has participated in the server in various ways.



