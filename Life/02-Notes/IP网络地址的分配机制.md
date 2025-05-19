---
category:
  - Tech
tags:
  - TCPIP
status: Done
---
公有网络地址的分配机制是由全球互联网地址注册机构和区域互联网注册机构共同管理和协调的。以下是公有网络地址的分配方式及其机制的详细解释：

**1. 公有网络地址的定义**

- **公有网络地址**是可以在全球互联网中路由和访问的IP地址，与私有地址不同，这些地址是唯一的，不会在不同的网络之间重叠。这种唯一性确保了设备可以在全球范围内进行通信。

**2. 地址分配的全球组织和机构**

公有网络地址的分配是由一系列机构负责协调和管理的：

- **IANA（Internet Assigned Numbers Authority，互联网号码分配局）**：

    -  IANA是负责管理全球IP地址和自治系统号码（ASN）的顶级机构，主要任务是将IP地址块分配给区域互联网注册机构（RIRs）。

- **RIRs（Regional Internet Registries，区域互联网注册机构）**：
  全球分为五大区域，每个区域由一个RIR负责管理和分配IP地址块。这五大RIR是：

    1. **ARIN（American Registry for Internet Numbers）**：负责北美地区。
    2. **RIPE NCC（Réseaux IP Européens Network Coordination Centre）**：负责欧洲、中东和中亚部分地区。
    3. **APNIC（Asia-Pacific Network Information Centre）**：负责亚太地区。
    4. **LACNIC（Latin American and Caribbean Internet Addresses Registry）**：负责拉丁美洲和加勒比地区。
    5. **AFRINIC（African Network Information Centre）**：负责非洲地区。

- **LIRs（Local Internet Registries，本地互联网注册机构）**：

    - LIR通常是ISP（互联网服务提供商）或大型企业，RIR会将地址分配给这些本地机构，它们再进一步将IP地址分配给最终用户，如公司和个人。

**3. 公有网络地址的分配机制**

**地址分配的过程**涉及到从顶级机构到最终用户的多级分配，具体机制如下：

1. **IANA分配**：
    - IANA将较大的IP地址块（如/8或/12）分配给RIRs。这些地址块被称为“父地址块”或“超级网段”。

2. **RIRs分配**：
    - RIRs根据各自区域内的IP地址需求，将地址块（如/16或/20）分配给LIRs（如ISP）或NIRs（National Internet Registries，国家互联网注册机构）。
    - RIRs基于申请机构的使用情况、计划以及地址耗尽情况，分配适量的地址。

3. **LIRs或ISP分配**：
    - ISP会将收到的地址块分配给其客户，包括企业、政府机构和个人用户。
    - 大型企业如果直接从RIR申请到地址，也会自己管理和使用这些公有地址。

4. **使用和管理**：
    - 分配的公有IP地址必须合理使用，申请机构通常需要提供详细的地址使用计划和扩展计划。
    - RIR和LIR会定期审查地址使用情况，以确保地址资源被有效利用。
  
**4. 公有地址分配的示例**

**示例流程**：

1. IANA将一个大块的地址空间（如192.0.0.0/8）分配给RIPE NCC。

2. RIPE NCC根据欧洲地区的需求，将一部分地址（如192.0.2.0/24）分配给某个ISP。

3. ISP将该地址空间进一步分配给公司客户（如192.0.2.128/25）。

