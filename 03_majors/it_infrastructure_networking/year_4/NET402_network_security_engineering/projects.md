# NET402 · Labs and projects

All work happens in your own isolated lab: Containerlab or VMs running OPNsense or nftables firewalls, FRRouting, FreeRADIUS or PacketFence, strongSwan and WireGuard, a Wazuh or Elastic collector, and the Windows domain and CA from NET302. Every lab starts with a one-paragraph scope statement. Scanning and flow tests target only lab addresses; never test a network you do not own or have written permission to test.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Threat model and scope | Threat model of the NET301 lab network; authorisation and scope document for the semester | Model, scope document | 3 h |
| 2 · Device hardening and AAA | Out-of-band management, TACACS+ with command accounting, CoPP, routing authentication, BCP 38, SNMPv3 only; automated 15-rule audit | Audit report before and after; spoofed-packet drop evidence | 5 h |
| 3 · Firewall policy and HA | Zone-based policy for a branch on OPNsense or nftables; active/passive pair with state sync; asymmetric-routing fault fixed | Policy export, failover test with session survival, fault write-up | 5 h |
| 4 · NGFW features and decryption policy | Application- and user-based rules; IPS in detect then prevent mode with tuning; a written TLS decryption policy with exceptions | Rule set, 3 tuned false positives, policy document | 4 h |
| 5 · Policy cleanup and policy as code | Clean a 200-rule policy with planted shadowed, redundant and broad rules; move policy to Git with CI that blocks any-any; review 10 AI-drafted rules with Batfish | Cleanup log, CI run, AI defect table | 6 h |
| 6 · Segmentation and flow tests | Five zones plus microsegmentation for a 3-tier app; 500 automated allowed/denied flow tests | Segmentation matrix, test results with zero unexplained outcomes | 5 h |
| 7 · 802.1X, MAB and RadSec | Wired EAP-TLS with AD certificates, MAB for headless devices, dynamic VLAN and CoA, Message-Authenticator enforced and RadSec between switch and server | Captures of each authentication type; CoA demonstration | 6 h |
| 8 · IKEv2, WireGuard and remote access | Route-based IKEv2 between sites with BGP, a WireGuard alternative, remote access with MFA; crypto inventory | Configs, tunnel failover times, crypto inventory table | 5 h |
| 9 · RTBH and DDoS runbook | RTBH and Flowspec signalling to a simulated ISP; firewall state-table protection under a load test against your own server | Route evidence, load-test results, tabletop notes | 4 h |
| 10 · Logging to SIEM | Syslog over TLS from all lab controls, NTP alignment, ECS normalisation, 180-day storage sizing, 5 detections | Log-loss test, sizing calculation, detection rules with test events | 5 h |

## Projects

### P1 · Hardening baseline and automated audit (L1, ~6 hours)

**Real-world inspiration.** The December 2024 CISA-led guidance for communications infrastructure starts with basics: separate management networks, default-deny ACLs, no plaintext services, SNMPv3 only. Many Indian enterprises and service providers are now asked by clients and auditors to show this evidence.

**What to build.** A written hardening standard for routers, switches and firewalls (management, control and data planes, logging and time), with each rule mapped to its source (CISA guidance, CIS Benchmark or vendor guide), and an automated audit (extend your NET303 P1 tool) that checks every rule on lab devices.

**Acceptance criteria**
- At least 20 rules, each with rationale, source, check method and remediation.
- The audit runs against at least 3 platforms and reports pass/fail per rule per device as JSON and a readable report.
- After remediation, all lab devices pass 100% of rules, or exceptions are documented with risk acceptance.
- The audit runs in CI and fails the build when a device drifts.

**Stretch goals.** Add evidence capture (configuration snippets) for auditors; map rules to CIS Controls safeguards.

**What it proves to an employer.** You can translate guidance into checkable engineering controls, the basis of every network security engineering role.

### P2 · Phased 802.1X and NAC rollout with secured RADIUS (L2, ~15 hours)

**Real-world inspiration.** Hospitals, universities and factories in India connect unmanaged and headless devices (infusion pumps, CCTV, lab instruments) next to staff laptops. A failed NAC rollout can lock clinicians out of systems; a missing one lets any device join the network. The site below (a 500-bed hospital, illustrative) is a composite.

**What to build.** A NAC design and working lab: EAP-TLS for managed Windows devices (certificates from NET302), MAB with profiling for 5 classes of headless devices, dynamic VLANs or downloadable ACLs per class, a guest flow, a remediation VLAN using CoA, RADIUS redundancy with a defined fallback when RADIUS is unreachable, Message-Authenticator enforcement and RadSec. Write a phased rollout plan (monitor → low impact → closed) with success criteria and a rollback per phase.

**Acceptance criteria**
- In monitor mode, a report lists every device that would fail authentication, with its class and the fix.
- In closed mode, each device class lands in its intended segment in 100% of 50 test connections, and unknown devices land in a restricted segment.
- Losing one RADIUS server causes no authentication failures; losing both triggers the documented fallback within 30 seconds.
- Configuration audits and captures show that every RADIUS client requires a valid Message-Authenticator on all responses, and that RadSec traffic is encrypted end to end.
- All NAC decisions reach the SIEM with device identity and result.

**Stretch goals.** Add MACsec on one uplink; add posture checks that move non-compliant laptops to remediation automatically.

**What it proves to an employer.** You can deploy access control in a real organisation without causing an outage, one of the most requested and most feared projects in enterprise networking.

### P3 · Segmented, logged and verified enterprise network with a security evidence pack (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** The government's reply on the 2022 AIIMS Delhi attack pointed to improper network segmentation; CERT-In requires 6-hour reporting and 180 days of logs; RBI directions require regulated entities to govern IT risk. The organisation below (a regional bank with a head office, a data centre and 30 branches, illustrative) must show its controls work, not just exist.

**What to build.** A complete defensive design and lab implementation: hardened devices (P1), zones and VRFs across campus, data centre and branches, an east-west firewall pair and microsegmentation for one critical application, a cleaned and version-controlled firewall policy with CI checks and Batfish analysis, NAC at the head office (P2), route-based IKEv2 VPNs to branches with a ZTNA path for one internal application, RTBH with a simulated ISP, central logging to a SIEM with 5 detections, and a bastion for all administration. Produce an evidence pack: segmentation matrix, automated test results, policy analysis output, log-coverage proof, and a mapping to CERT-In directions and CIS Controls.

**Acceptance criteria**
- At least 1,000 automated flow tests pass with zero unexplained results, covering every cell of the segmentation matrix.
- Batfish proves that no path exists from the guest or IoT zones to the core banking zone, and that every permitted flow has an owner and expiry in the policy repository.
- A change that would open an any-any rule is blocked by CI.
- Log coverage: every control type sends logs with synchronised time; a collector restart loses no events (verified by sequence numbers or counts).
- In a tabletop and lab exercise of a compromised branch VPN gateway, the compromised zone is contained within 15 minutes using pre-written steps, and the CERT-In reporting decision is made and logged within the exercise.
- An AI assistant is evaluated on 15 policy tasks against Batfish; its error types are reported, and no AI-drafted rule reaches the firewall without passing CI.

**Stretch goals.** Add post-quantum hybrid IKEv2 where your VPN software supports it and measure the handshake cost; add a dashboard showing control health for managers.

**What it proves to an employer.** You can engineer network security controls and prove they work with evidence that auditors, regulators and SOC teams accept, which is senior network security engineer work.

## Feeds into

- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): P3 is a strong capstone base.
- The [OV01 Cloud Security](../../../../04_overlaps/OV01_cloud_security/README.md) and [OV03 DevSecOps](../../../../04_overlaps/OV03_devsecops/README.md) overlaps.
- [SEC302 Security Operations](../../../cybersecurity_defense/year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md) and [SAR303 Zero Trust Architecture](../../../security_architecture/year_3/SAR303_zero_trust_architecture/README.md) as electives.
- [NET403 AIOps and Intent-Based Networking](../NET403_aiops_and_intent_based_networking/README.md): security intent becomes verifiable policy.
