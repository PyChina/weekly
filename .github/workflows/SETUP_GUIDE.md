# GitHub Pages 部署配置指南

## 🔴 部署失败的常见原因

如果你看到类似以下的错误：
```
Error: Creating Pages deployment failed
Error: HttpError: Not Found
```

或者：
```
Error: Ensure GITHUB_TOKEN has permission "pages: write".
```

这是因为 GitHub 仓库的 Pages 设置没有正确配置。

---

## ✅ 解决步骤

### 步骤 1: 启用 GitHub Pages

1. 打开仓库页面：`https://github.com/PyChina/weekly`
2. 点击 **Settings** 标签
3. 左侧菜单点击 **Pages**
4. 在 **Build and deployment** 部分：
   - **Source**: 选择 **GitHub Actions**
   
   ![source selection](https://docs.github.com/assets/images/help/pages/pages-source-github-actions.png)

> ⚠️ **重要**: 不要选择 "Deploy from a branch"，必须选择 **GitHub Actions**

---

### 步骤 2: 检查 Workflow 权限

1. 在 Settings 页面，点击左侧 **Actions** → **General**
2. 找到 **Workflow permissions** 部分：
   - 选择 **Read and write permissions**
   - 勾选 **Allow GitHub Actions to create and approve pull requests**

---

### 步骤 3: 重新运行工作流

配置完成后：

1. 进入 **Actions** 标签页
2. 找到失败的 workflow run
3. 点击 **Re-run jobs** → **Re-run all jobs**

或者推送一个新的 commit 触发新的部署：
```bash
git commit --allow-empty -m "触发重新部署"
git push
```

---

## 📋 完整的 GitHub 设置检查清单

| 设置项 | 路径 | 应该设置为 |
|--------|------|-----------|
| Pages Source | Settings → Pages → Source | GitHub Actions |
| Workflow 权限 | Settings → Actions → General | Read and write permissions |
| 环境保护规则 | Settings → Environments | 无（或允许 github-pages 分支） |

---

## 🔧 如果仍然失败

### 检查 Environment 设置

有些仓库需要配置 Environment：

1. Settings → Environments
2. 点击 **github-pages**（如果没有就创建一个）
3. 确保没有设置 **Deployment protection rules**，或暂时关闭 "Required reviewers"

### 检查 Token 权限

确保使用的是 `GITHUB_TOKEN` 而不是 `DEPLOY_TOKEN`：

```yaml
# 工作流中应该使用默认的 GITHUB_TOKEN
permissions:
  pages: write
  id-token: write
```

不需要在 Secrets 中设置任何 token。

---

## 📖 参考文档

- [GitHub Pages 文档](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [Deploy Pages Action](https://github.com/actions/deploy-pages)
- [Upload Pages Artifact](https://github.com/actions/upload-pages-artifact)
