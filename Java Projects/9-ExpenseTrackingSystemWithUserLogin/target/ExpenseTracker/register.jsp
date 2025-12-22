<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <title>Register - Expense Tracker</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-5">
                <h3 class="text-center mb-4">Register</h3>
                <form action="RegisterServlet" method="post" onsubmit="return validateForm()">
                    <div class="mb-3">
                        <label>Name</label>
                        <input type="text" name="name" id="name" class="form-control" required>
                    </div>
                    <div class="mb-3">
                        <label>Email</label>
                        <input type="email" name="email" id="email" class="form-control" required>
                    </div>
                    <div class="mb-3">
                        <label>Password</label>
                        <input type="password" name="password" id="password" class="form-control" required>
                    </div>
                    <div id="error" class="text-danger mb-2"></div>
                    <button type="submit" class="btn btn-success w-100">Register</button>
                </form>
                <p class="text-center mt-3">Already registered? <a href="login.jsp">Login</a></p>
            </div>
        </div>
    </div>

    <script>
        function validateForm() {
            const name = document.getElementById("name").value.trim();
            const email = document.getElementById("email").value.trim();
            const password = document.getElementById("password").value.trim();
            const errorDiv = document.getElementById("error");

            if (!name || !email || !password) {
                errorDiv.textContent = "All fields are required!";
                return false;
            }

            if (!email.includes("@")) {
                errorDiv.textContent = "Enter a valid email!";
                return false;
            }

            return true;
        }
    </script>
</body>
</html>
