# GitHub Actions 自动化部署

## 概述

此 GitHub Actions 工作流替代了原有的 `inv pub` 命令，实现了自动化构建和部署。

## 触发条件

工作流在以下情况下触发：
- 推送到 `master` 或 `main` 分支
- 修改了 `content/` 目录下的文件
- 修改了主题或配置文件
- 手动触发（workflow_dispatch）

## 工作流程

```
┌─────────────┐
│   Push 代码  │
└──────┬──────┘
       ▼
┌─────────────┐
│ 检出代码    │
└──────┬──────┘
       ▼
┌─────────────┐
│ 安装依赖    │
└──────┬──────┘
       ▼
┌─────────────┐     有警告     ┌─────────────┐
│ 首次构建    │───────────────▶│ 修复图片alt │
└──────┬──────┘                └──────┬──────┘
       │ 无警告                        │
       ▼                               ▼
┌─────────────┐                ┌─────────────┐
│ 检查完成    │◀───────────────│ 提交修复    │
└──────┬──────┘                └─────────────┘
       ▼
┌─────────────┐
│ 部署到Pages │
└─────────────┘
```

## 功能特点

1. **自动修复图片 alt 属性**
   - 检测缺少 alt 属性的图片
   - 根据图片文件名自动生成 alt 文本
   - 提交修复后重新构建

2. **零配置部署**
   - 使用 GitHub Pages 官方部署机制
   - 无需手动管理 `output` 分支

3. **并发控制**
   - 使用 concurrency 防止并发构建冲突

## 迁移说明

### 之前的工作流程 (inv pub)

```bash
inv pub
# 执行:
# 1. git pull
# 2. pelican build
# 3. git commit content
# 4. git commit output
# 5. git push
```

### 新的工作流程

1. 本地编辑 Markdown 文件
2. 提交并推送: `git add . && git commit -m "..." && git push`
3. GitHub Actions 自动完成构建和部署

## 本地测试

```bash
# 安装依赖
pip install pelican markdown beautifulsoup4

# 本地构建
pelican content -o output -s pelicanconf.py

# 本地预览
cd output && python -m http.server
```

## 故障排查

### 构建失败

查看 GitHub Actions 日志：
1. 进入仓库的 Actions 标签页
2. 点击失败的 workflow run
3. 查看具体步骤的日志

### 图片 alt 警告

如果收到图片 alt 警告，工作流会自动修复并重新提交。你可以在提交历史中看到这些自动修复。

### 手动触发

如果需要手动触发部署：
1. 进入 Actions 标签页
2. 选择 "Build and Deploy Weekly"
3. 点击 "Run workflow"
