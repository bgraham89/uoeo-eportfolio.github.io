# Attack Tree

```mermaid
graph LR;
  root((("`root
`"))) --- Spoofing(("`Spoofing
Likelihood: 22`"));
  Spoofing(("`Spoofing
Likelihood: 22`")) --- FakeOrders{{"`Fake Orders
Likelihood: 10`"}};
  Spoofing(("`Spoofing
Likelihood: 22`")) --- FakeServices{{"`Fake Services
Likelihood: 1`"}};
  Spoofing(("`Spoofing
Likelihood: 22`")) --- TrademarkInfringement{{"`Trademark Infringement
Likelihood: 5`"}};
  Spoofing(("`Spoofing
Likelihood: 22`")) --- HotspotEvilTwin{{"`Hotspot Evil Twin
Likelihood: 1`"}};
  Spoofing(("`Spoofing
Likelihood: 22`")) --- TargetedUserSpoofing{{"`Targeted User Spoofing
Likelihood: 5`"}};
  root((("`root
`"))) --- Tampering(("`Tampering
`"));
  Tampering(("`Tampering
`")) --- PhysicalDamage{{"`Physical Damage
`"}};
  Tampering(("`Tampering
`")) --- MerchandiseModification{{"`Merchandise Modification
`"}};
  Tampering(("`Tampering
`")) --- InformationModification{{"`Information Modification
`"}};
  Tampering(("`Tampering
`")) --- InformationDeletion{{"`Information Deletion
`"}};
  Tampering(("`Tampering
`")) --- TargetedUserTampering{{"`Targeted User Tampering
`"}};
  root((("`root
`"))) --- Repudiation(("`Repudiation
`"));
  Repudiation(("`Repudiation
`")) --- EmailAnonymity{{"`Email Anonymity
`"}};
  Repudiation(("`Repudiation
`")) --- MissingBackupSystem{{"`Missing Backup System
`"}};
  Repudiation(("`Repudiation
`")) --- MissingLoggingSystem{{"`Missing Logging System
`"}};
  root((("`root
`"))) --- InformationDisclosure(("`Information Disclosure
`"));
  InformationDisclosure(("`Information Disclosure
`")) --- UnauthorisedAccesstoComputers{{"`Unauthorised Access to Computers
`"}};
  InformationDisclosure(("`Information Disclosure
`")) --- UnauthorisedAccesstoPhones{{"`Unauthorised Access to Phones
`"}};
  InformationDisclosure(("`Information Disclosure
`")) --- UnauthorisedAccesstoUserInformation{{"`Unauthorised Access to User Information
`"}};
  root((("`root
`"))) --- DenialofService(("`Denial of Service
`"));
  DenialofService(("`Denial of Service
`")) --- LossofSupply{{"`Loss of Supply
`"}};
  DenialofService(("`Denial of Service
`")) --- LossofElectricity{{"`Loss of Electricity
`"}};
  DenialofService(("`Denial of Service
`")) --- LossofInternet{{"`Loss of Internet
`"}};
  DenialofService(("`Denial of Service
`")) --- StaffDisruption{{"`Staff Disruption
`"}};
  DenialofService(("`Denial of Service
`")) --- RegulationFailure{{"`Regulation Failure
`"}};
  DenialofService(("`Denial of Service
`")) --- DDOSBusinessVPN{{"`DDOS Business VPN
`"}};
  root((("`root
`"))) --- EscalationofPrivilege(("`Escalation of Privilege
`"));
  EscalationofPrivilege(("`Escalation of Privilege
`")) --- MisguidedTrust{{"`Misguided Trust
`"}};
  EscalationofPrivilege(("`Escalation of Privilege
`")) --- UnauthorisedInformationAccess{{"`Unauthorised Information Access
`"}};
  EscalationofPrivilege(("`Escalation of Privilege
`")) --- ViralIncident{{"`Viral Incident
`"}};
```
