<?php
// Set email address where the form data will be sent
$to = "youremail@example.com";

// Get form data
$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];

// Set email headers
$headers = "From: $name <$email>\r\n";
$headers .= "Reply-To: $name <$email>\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/html; charset=UTF-8\r\n";

// Construct email body
$body = "<h2>New message from the Popup Form</h2>";
$body .= "<p><strong>Name:</strong> $name</p>";
$body .= "<p><strong>Email:</strong> $email</p>";
$body .= "<p><strong>Message:</strong><br>$message</p>";

// Send email
if (mail($to, "New message from the Popup Form", $body, $headers)) {
    echo "success";
} else {
    echo "error";
}
?>