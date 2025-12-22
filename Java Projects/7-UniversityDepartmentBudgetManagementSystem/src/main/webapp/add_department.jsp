<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Add Department</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <div class="card shadow">
            <div class="card-header bg-info text-white">
                <h4 class="mb-0">Add Department</h4>
            </div>
            <div class="card-body">
                <form action="addDepartment" method="post">
                    <div class="form-group">
                        <label for="name">Department Name</label>
                        <input type="text" class="form-control" name="name" id="name" required>
                    </div>
                    <div class="form-group">
                        <label for="head">Head of Department</label>
                        <input type="text" class="form-control" name="head" id="head" required>
                    </div>
                    <button type="submit" class="btn btn-primary">Add Department</button>
                    <a href="index.jsp" class="btn btn-secondary ml-2">Back</a>
                </form>
            </div>
        </div>
    </div>
</body>
</html>
