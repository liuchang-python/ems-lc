<template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        2009/11/20
                        <br/>
                    </p>
                </div>
                <div id="topheader">
                    <h1 id="title">
                        <a href="#">Main</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>
            <div id="content">
                <p id="whereami">
                </p>
                <h1>
                    add Emp info:
                </h1>
                <table cellpadding="0" cellspacing="0" border="0"
                       class="form_table">
                    <tr>
                        <td valign="middle" align="right">
                            name:
                        </td>
                        <td valign="middle" align="left">
                            <input v-model="username" type="text" class="inputgri" name="name"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            photo:
                        </td>
                        <td valign="middle" align="left">
                            <input ref="photo" type="file" name="photo"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            salary:
                        </td>
                        <td valign="middle" align="left">
                            <input v-model="salary" type="text" class="inputgri" name="salary"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            age:
                        </td>
                        <td valign="middle" align="left">
                            <input v-model="age" type="text" class="inputgri" name="age"/>
                        </td>
                    </tr>
                </table>
                <p><el-button type="primary" @click="add_emp">确定添加</el-button>
                    <el-button type="primary" @click="to_last_page">返回上一页</el-button>
                </p>
            </div>
        </div>
        <div id="footer">
            <div id="footer_bg">
                ABC@126.com
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "AddEmp",
    data() {
        return {
            username: "",
            photo: "",
            salary: "",
            age: "",
        }
    },
    methods: {
        // 添加员工
        add_emp() {
            let formData = new FormData();
            formData.append("emp_name", this.username)
            formData.append("salary", this.salary)
            formData.append("age", this.age)
            formData.append("img", this.$refs.photo.files[0])
            this.$axios({
                url: "http://127.0.0.1:8000/api/employee/",
                method: "post",
                data: formData,
                headers: {
                    "content-type": "multipart/form-data"
                },
            }).then(res => {
                this.$router.push("/index");
            }).catch(error => {
                console.log(error);
            })
        },
        to_last_page() {
            this.$router.go(-1);
        }
    }
}
</script>

<style scoped>

</style>
