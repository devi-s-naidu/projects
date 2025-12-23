<?php
session_start();
include "db.php";

if(isset($_POST["email"]) && isset($_POST["password"])) {
    $email = mysqli_real_escape_string($con,$_POST["email"]);
    $password = $_POST["password"];

    $sql = "SELECT * FROM admin_info WHERE admin_email = '$email' AND admin_password = '$password'";
    $run_query = mysqli_query($con,$sql);
    $count = mysqli_num_rows($run_query);

    if($count == 1) {
        $row = mysqli_fetch_array($run_query);
        $_SESSION["a_id"] = $row["admin_id"];
        $_SESSION["a_name"] = $row["admin_name"];
        $ip_add = getenv("REMOTE_ADDR");

        // Redirect to admin page after successful login
        header("Location: index.php");
        exit;
    } else {
        $login_error = "Invalid email or password. Please try again.";
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #ccc; /* Gray background */
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .login-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            width: 100%;
        }

        .login-container h2 {
            margin-top: 0;
            text-align: center;
            color: #333;
        }

        .login-form input[type="email"],
        .login-form input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 3px;
            box-sizing: border-box;
        }

        .login-form input[type="submit"] {
            width: 100%;
            padding: 10px;
            background-color: #ff0000; /* Red background */
            border: none;
            border-radius: 3px;
            color: #fff;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .login-form input[type="submit"]:hover {
            background-color: #cc0000; /* Darker red on hover */
        }

        .error-message {
            color: red;
            text-align: center;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Login</h2>
        <?php
        if(isset($login_error)) {
            echo "<p class='error-message'>$login_error</p>";
        }
        ?>
        <form class="login-form" method="post" action="">
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" required><br>
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password" required><br><br>
            <input type="submit" value="Login">
        </form>
    </div>
</body>
</html>
