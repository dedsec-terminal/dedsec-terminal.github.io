---
title: "Microsoft Releases Mitigation for YellowKey BitLocker Bypass CVE-2026-45585 Exploit"
date: 2026-05-20T08:28:26+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Microsoft has released a mitigation for a zero-day vulnerability in BitLocker, known as YellowKey, which was publicly disclosed last week. The vulnerability, tracked as CVE-2026-45585, carries a CVSS score of 6.8 and allows an attacker with physical access to bypass the BitLocker Device Encryption feature on a system storage device, gaining access to encrypted data. This is achieved by placing specially crafted 'FsTx' files on a USB drive or EFI partition, rebooting into the Windows Recovery Environment, and triggering a shell with unrestricted access.

The issue affects various versions of Windows 11 and Windows Server 2025, and successful exploitation could permit an attacker to sidestep BitLocker protections and access encrypted data. The vulnerability abuses a behavioral trust assumption in the recovery interface, allowing attackers to spawn an unrestricted shell with full access to the encrypted volume during the pre-boot recovery sequence. This means that any machine with a USB port and the ability to be rebooted can be a target, as no software installation, existing credentials, or network access is required to break encryption.

To address the risk, Microsoft has outlined several mitigations, including modifying the BootExecute registry value to prevent the FsTx Auto Recovery Utility from automatically starting when the Windows Recovery Environment image launches. Additionally, users can safeguard against exploitation by configuring BitLocker on already encrypted devices to use "TPM+PIN" mode, which requires a PIN to decrypt the drive at startup. This can be done via PowerShell, the command line, or the control panel. On devices that are not encrypted, administrators are advised to enable the "Require additional authentication at startup" option and ensure that "Configure TPM startup PIN" is set to "Require startup PIN with TPM".

The mitigation involves a series of steps, including mounting the WinRE image, modifying the system registry hive, and reestablishing BitLocker trust for WinRE. By following these steps, users can prevent the YellowKey exploit from succeeding. It is also recommended to switch from TPM-only to TPM+PIN mode to add an extra layer of security. By taking these measures, users can protect their encrypted data from being accessed by attackers using the YellowKey vulnerability.

Microsoft's mitigation provides a way to prevent the YellowKey exploit from being used to bypass BitLocker protections. By applying the recommended mitigations, users can ensure that their encrypted data remains secure, even in the event of physical access to the device. It is essential for users to take immediate action to protect their

---

> *All the great performers I have worked with are fuelled by a personal dream.
Author: John Eliot*

Source: [Microsoft Releases Mitigation for YellowKey BitLocker Bypass CVE-2026-45585 Exploit](https://thehackernews.com/2026/05/microsoft-releases-mitigation-for.html)
