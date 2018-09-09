<?php
  $this->info = array(
    // OSF project info
    'projectId' => '',
    'projectName' => 'blockedTrials',
    // OSF server URL
    "osfUrl" => "https://api.osf.io/v2/",
    // experimenter's OSF security token for this project
    "token" => undefined,
    // name of resource directory for this project on OSF server
    "osfResourceDirectory" => "html/resources",


    // name of the directory containing the experiment's resources,
    // both on the local experiment server and on the remote OSF server
    "resourceDirectory" => "resources",
    // name of the directory containing the participant's data,
    // both on the local experiment server and on the remote OSF server
    "dataDirectory" => "data",


    // experimenter contact details
    'experimenterEmail' => '',
    // SMTP server settings:
    'smtpServer' => '',
    'smtpUsername' => '',
    'smtpPassword' => '',
    'smtpSecure' => 'tls', // 'ssl'
    'smtpTcpPort' => 587
  );
?>