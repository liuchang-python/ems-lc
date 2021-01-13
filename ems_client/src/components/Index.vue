<template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        2009/11/20
                        <br/>
                        <el-button size="small" type="primary" plain @click="log_out">安全退出</el-button>
                    </p>
                </div>
                <div id="topheader">
                    <h1 id="title">
                        <a href="#">main</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>
            <div id="content">
                <p id="whereami">
                </p>
                <h1>
                    Welcome! {{ this.username }}
                </h1>
                <table class="table">
                    <tr class="table_header">
                        <td>ID</td>
                        <td>Name</td>
                        <td>Photo</td>
                        <td>Salary</td>
                        <td>Age</td>
                        <td>Operation</td>
                    </tr>
                    <tr class="row2" v-for="emp in emp_list" :key="emp.id">
                        <td>{{ emp.id }}</td>
                        <td>{{ emp.emp_name }}</td>
                        <td width="240"><img :src=emp.full_img style="height: 120px;"></td>
                        <td>{{ emp.salary }}</td>
                        <td>{{ emp.age }}</td>
                        <td>
                            <el-button type="primary" @click="del_emp(emp.id)" size="small">删除员工</el-button>
                            <el-button type="primary" @click="alter_emp(emp.id)" size="small">更新员工</el-button>
                        </td>
                    </tr>
                </table>
                <p>
                    <el-button type="primary" @click="to_add">
                        添加员工
                    </el-button>
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
    name: "Index",
    data() {
        return {
            emp_list: [],
            username: ''
        }
    },
    methods: {
        get_all_emp() {
            let username = sessionStorage.getItem("username")
            if (username) {
                this.$axios.get("http://127.0.0.1:8000/api/employee/").then(res => {
                    console.log(res.data);
                    this.emp_list = res.data;
                    this.username = username;
                }).catch(error => {
                    console.log(error);
                })
            } else {
                this.$message.error("当前用户未登录,请登录");
                this.$router.push("/login");
            }
        },
        to_add() {
            this.$router.push('/add');
        },
        alter_emp(id) {
            this.$router.push('/update/' + id);
        },
        del_emp(id) {
            this.$axios.delete("http://127.0.0.1:8000/api/employee/" + id).then(res=>{
                console.log(res);
                this.$router.go(0);
            })
        },
        log_out(){
            sessionStorage.removeItem('username');
            // sessionStorage.clear();
            this.$router.push('/login');
        },

    },
    created() {
        this.get_all_emp();
    }
}
</script>

<style scoped>

</style>
