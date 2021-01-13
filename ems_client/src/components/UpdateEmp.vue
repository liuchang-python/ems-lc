<template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>2009/11/20
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
                <p id="whereami"></p>
                <h1>update Emp info:</h1>
                <form action="emplist.html" method="post">
                    <table cellpadding="0" cellspacing="0" border="0"
                           class="form_table">
                        <tr>
                            <td valign="middle" align="right">id:</td>
                            <td valign="middle" align="left">{{emp.id}}</td>
                        </tr>
                        <tr><td valign="middle" align="right">name:</td>
                            <td valign="middle" align="left">
                                <input v-model="emp.emp_name" type="text" class="inputgri" name="name" value="zhangshan"/>
                            </td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">photo:</td>
                            <td valign="middle" align="left"><input ref="photo" type="file" name="photo"/></td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">salary:</td>
                            <td valign="middle" align="left"><input v-model="emp.salary" type="text" class="inputgri" name="salary" value="20000"/></td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">age:</td>
                            <td valign="middle" align="left"><input v-model="emp.age" type="text" class="inputgri" name="age" value="20"/></td>
                        </tr>
                    </table>
                    <p>
                        <el-button type="primary" @click="alter_emp">确定更新</el-button>
                        <el-button type="primary" @click="to_last_page">
                            返回上一页
                        </el-button>
                    </p>
                </form>
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
    name: "UpdateEmp",
    data(){
        return {
            emp:{},
        }
    },
    methods:{
        alter_emp(){
            let formData = new FormData();
            formData.append("emp_name", this.emp.emp_name)
            formData.append("salary", this.emp.salary)
            formData.append("age", this.emp.age)
            formData.append("img", this.$refs.photo.files[0])
            console.log(this.$refs.photo.files[0])

            let emp_id = this.$route.params.id
            this.$axios.patch("http://127.0.0.1:8000/api/employee/" + emp_id, formData).then(res => {
                console.log(res.data);
                this.$router.push('/index')
            }).catch(error => {
                console.log(error);
            })
        },
        to_last_page() {
            this.$router.go(-1);
        },
        get_emp(){
            let username = sessionStorage.getItem("username")
            if (username) {
                let emp_id = this.$route.params.id
                this.$axios.get("http://127.0.0.1:8000/api/employee/"+emp_id).then(res => {
                    console.log(res.data);
                    this.emp = res.data;
                    this.username = username;
                }).catch(error => {
                    console.log(error);
                })
            } else {
                this.$message.error("当前用户未登录,请登录");
                this.$router.push("/login");
            }
        },
    },
    created() {
        this.get_emp();
    }
}
</script>

<style scoped>

</style>
