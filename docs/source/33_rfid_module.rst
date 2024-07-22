17. Exploring the I2C LCD1602 Display
================================================

  
In this lesson, you will learn how to use an RFID Module. RFID stands for Radio Frequency Identification. Its principle of operation involves contactless data communication between the reader and the label to identify the target. The applications of RFID are extensive, including animal chips, immobilizers, access control, parking control, production chain automation, material management, and more.

.. raw:: html

    <video width="600" loop autoplay muted>
        <source src="_static/video/30_servo_radar.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
  
Build the Circuit
------------------------------------

**Components Needed**

.. list-table:: 
   :widths: 25 25 25 25
   :header-rows: 0

   * - 1 * Arduino Uno R3
     - 1 * RFID Module and Card
     - 1 * Breadboard
     - 1 * USB Cable
   * - |components_uno_r3|
     - |components_i2c_lcd1602| 
     - |components_breadboard|
     - |components_usb_cable|
   * - Jumper Wires
     - 
     - 
     - 
   * - |components_wire|
     - 
     - 
     - 

**Building Steps**

Follow the wiring diagram, or the steps below to build your circuit.

.. image:: img/17_lcd_connect.png
    :width: 700
    :align: center

**RFID**

Radio Frequency Identification (RFID) refers to technologies that involve using wireless communication between an object (or tag) and an interrogating device (or reader) to automatically track and identify such objects. The tag transmission range is limited to several meters from the reader. A clear line of sight between the reader and tag is not necessarily required.

Most tags contain at least one integrated circuit (IC) and an antenna. The microchip stores information and is responsible for managing the radio frequency (RF) communication with the reader. Passive tags do not have an independent energy source and depend on an external electromagnetic signal, provided by the reader, to power their operations. Active tags contain an independent energy source, such as a battery. Thus, they may have increased processing, transmission capabilities and range.

.. image:: img/mfrc522.png

**MFRC522**

MFRC522 is a kind of integrated read and write card chip. It is commonly used in the radio at 13.56MHz. Launched by the NXP Company, it is a low-voltage, low-cost, and small-sized non-contact card chip, a best choice of intelligent instrument and portable handheld device.

The MF RC522 uses advanced modulation and demodulation concept which fully presented in all types of 13.56MHz passive contactless communication methods and protocols. In addition, it supports rapid CRYPTO1 encryption algorithm to verify MIFARE products. MFRC522 also supports MIFARE series of high-speed non-contact communication, with a two-way data transmission rate up to 424kbit/s. As a new member of the 13.56MHz highly integrated reader card series, MF RC522 is much similar to the existing MF RC500 and MF RC530 but there also exists great differences. It communicates with the host machine via the serial manner which needs less wiring. You can choose between SPI, I2C and serial UART mode (similar to RS232), which helps reduce the connection, save PCB board space (smaller size), and reduce cost.


Code Creation - Write and Read
---------------------------------------
在这里，我们将安装使用MFRC522 RFID module所需的库，然后打开示例代码来给卡写入信息，以及从卡读取信息。

**写入信息**

1. To use the MFRC522 RFID module, you need to include the appropriate library. Now, search for ``MFRC522`` on the **Library Manager**, then click **INSTALL**.

.. image:: img/31_rfid_install_lib.png
  :align: center

2. 现在通过点击**File** -> **Examples** -> **MFRC522**，你会看到多个可以实现不同效果的示例代码，现在来打开``rfid_write_personal_data``的示例代码。

.. image:: img/33_rfid_open_write.png
  :align: center

3. 点击Upload来将它上传到你的Arduino板上。然后打开串行监视器，你会看到一句提示。

.. image:: img/33_rfid_write_open.png
  :align: center

4. 现在将配套的白卡或者是tag靠在MFRC522模块上，你将会看到这个卡的UID，PICC类型，以及提示你输出Family name, 输完之后需要跟一个#。

.. code-block::

  Write personal data on a MIFARE PICC 
  Card UID: 9B 2F 0A 11 PICC type: MIFARE 1KB
  Type Family name, ending with #

5. 现在来开始输入，比如我输入的是 ``XIE#``, 按下``Enter``键来将你的输入发送到Arduino板, 再传输到RFID模块上。

.. note::

  在你输入过程中，你需要确保你的卡是靠着RFID模块的磁片区，如果移开了将会报错。

.. image:: img/33_rfid_write_first_name.png
  :align: center

6. 接下来你看到成功写入的提示，并且要你写入first name的提示。

.. code-block::

  Write personal data on a MIFARE PICC 
  Card UID: 9B 2F 0A 11 PICC type: MIFARE 1KB
  Type Family name, ending with #
  PCD_Authenticate() success: 
  MIFARE_Write() success: 
  MIFARE_Write() success: 
  Type First name, ending with #

7. 接下来输入first name，比如我写的是``Daisy#``, 再次提示写入成功。

.. code-block::

  Write personal data on a MIFARE PICC 
  Card UID: 9B 2F 0A 11 PICC type: MIFARE 1KB
  Type Family name, ending with #
  PCD_Authenticate() success: 
  MIFARE_Write() success: 
  MIFARE_Write() success: 
  Type First name, ending with #
  MIFARE_Write() success: 
  MIFARE_Write() success: 

**读取信息**

刚才我们已经将自己的姓名写入到卡中了，现在打开另外一个示例代码来读取这张卡的信息，看下写入的信息是否存在。

1. 同样通过点击 **File** -> **Examples** -> **MFRC522**，打开``rfid_read_personal_data``的示例代码。

.. image:: img/33_rfid_read_open.png
  :align: center

2. 打开之后，将代码上传到你的Arduino板。然后将你的卡靠近RFID模块的磁片区，你将会看到你的UID以及刚才写入的姓名信息。

.. code-block::

  **Card Detected:**
  Card UID: 9B 2F 0A 11
  Card SAK: 08
  PICC type: MIFARE 1KB
  Name: 
  Daisy XIE             
  **End Reading**

Code Creation - 显示到LCD上
---------------------------------------

