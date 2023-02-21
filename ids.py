from common import Projects, ChartType, TaskType, SummaryTableColumn

MAIN_TASKS_LIST = "MAIN_TASKS_LIST_HEADER"

BLOCKERS_LIST = "BLOCKERS_LIST_HEADER"

WML_BUILD_LINK = "WML_BUILD_LINK"


SUMMARY_TABLE = {
    Projects.MAYA_RPR: {
        SummaryTableColumn.FOUND_ISSUES : "MAYA_RPR_SUMMARY_TABLE_FOUND_ISSUES",
        SummaryTableColumn.MERGED_PRS: "MAYA_RPR_SUMMARY_TABLE_MERGED_PRS"
    },
    Projects.MAYA_USD: {
        SummaryTableColumn.FOUND_ISSUES : "MAYA_USD_SUMMARY_TABLE_FOUND_ISSUES",
        SummaryTableColumn.MERGED_PRS: "MAYA_USD_SUMMARY_TABLE_MERGED_PRS"
    },
    Projects.BLENDER_RPR: {
        SummaryTableColumn.FOUND_ISSUES : "BLENDER_RPR_SUMMARY_TABLE_FOUND_ISSUES",
        SummaryTableColumn.MERGED_PRS: "BLENDER_RPR_SUMMARY_TABLE_MERGED_PRS"
    },
    Projects.BLENDER_USD: {
        SummaryTableColumn.FOUND_ISSUES : "BLENDER_USD_SUMMARY_TABLE_FOUND_ISSUES",
        SummaryTableColumn.MERGED_PRS: "BLENDER_USD_SUMMARY_TABLE_MERGED_PRS"
    },
    Projects.RENDER_STUDIO: {
        SummaryTableColumn.FOUND_ISSUES : "RENDER_STUDIO_SUMMARY_TABLE_FOUND_ISSUES",
        SummaryTableColumn.MERGED_PRS: "RENDER_STUDIO_SUMMARY_TABLE_MERGED_PRS"
    },
    Projects.HOUDINI: {
        SummaryTableColumn.FOUND_ISSUES : "HOUDINI_SUMMARY_TABLE_FOUND_ISSUES",
        SummaryTableColumn.MERGED_PRS: "HOUDINI_SUMMARY_TABLE_MERGED_PRS"
    }
}

BUILD_STATUS_TABLE_ROW = {
    Projects.MAYA_RPR: "MAYA_RPR_BUILD_STATUS_TABLE_ROW",
    Projects.MAYA_USD: "MAYA_USD_BUILD_STATUS_TABLE_ROW",
    Projects.BLENDER_RPR: "BLENDER_RPR_BUILD_STATUS_TABLE_ROW",
    Projects.BLENDER_USD: "BLENDER_USD_BUILD_STATUS_TABLE_ROW",
    Projects.HOUDINI: "HOUDINI_BUILD_STATUS_TABLE_ROW",
    Projects.RENDER_STUDIO: "RENDER_STUDIO_BUILD_STATUS_TABLE_ROW",
    Projects.HDRPR: "HDRPR_BUILD_STATUS_TABLE_ROW",
    Projects.SOLIDWORKS: "SOLIDWORKS_BUILD_STATUS_TABLE_ROW",
    Projects.MATERIALX: "MATERIALX_BUILD_STATUS_TABLE_ROW",
    Projects.USD_VIEWER_INVENTOR: "USD_VIEWER_INVENTOR_BUILD_STATUS_TABLE_ROW",
    Projects.ANARI: "ANARI_BUILD_STATUS_TABLE_ROW",
    Projects.BLENDER_HIP: "BLENDER_HIP_BUILD_STATUS_TABLE_ROW",
}

PR_STATUS_TABLE_ID = {
    Projects.MAYA_RPR: "MAYA_RPR_PR_STATUS_TBL",
    Projects.MAYA_USD: "MAYA_USD_PR_STATUS_TBL",
    Projects.BLENDER_RPR: "BLENDER_RPR_PR_STATUS_TBL",
    Projects.BLENDER_USD: "BLENDER_USD_PR_STATUS_TBL",
    Projects.HOUDINI: "HOUDINI_PR_STATUS_TBL",
    Projects.RENDER_STUDIO: "RENDER_STUDIO_PR_STATUS_TBL",
}

BUGS_LINK_ID = {
    Projects.MAYA_RPR: "MAYA_RPR_BUGS_LINK",
    Projects.MAYA_USD: "MAYA_USD_BUGS_LINK",
    Projects.BLENDER_RPR: "BLENDER_RPR_BUGS_LINK",
    Projects.BLENDER_USD: "BLENDER_USD_BUGS_LINK",
    Projects.RENDER_STUDIO: "RENDER_STUDIO_BUGS_LINK",
    Projects.HOUDINI: "HOUDINI_BUGS_LINK",
}

CHART_ID = {
    Projects.MAYA_RPR: {
        ChartType.UNRESOLVED_ISSUES: "MAYA_RPR_CHART_UNRESOLVED_ISSUES",
        ChartType.ISSUES_UPDATES_2W: "MAYA_RPR_CHART_ISSUES_UPDATES_2W",
    },
    Projects.MAYA_USD: {
        ChartType.UNRESOLVED_ISSUES: "MAYA_USD_CHART_UNRESOLVED_ISSUES",
        ChartType.ISSUES_UPDATES_2W: "MAYA_USD_CHART_ISSUES_UPDATES_2W",
    },
    Projects.BLENDER_RPR: {
        ChartType.UNRESOLVED_ISSUES: "BLENDER_RPR_CHART_UNRESOLVED_ISSUES",
        ChartType.ISSUES_UPDATES_2W: "BLENDER_RPR_CHART_ISSUES_UPDATES_2W",
    },
    Projects.BLENDER_USD: {
        ChartType.UNRESOLVED_ISSUES: "BLENDER_USD_CHART_UNRESOLVED_ISSUES",
        ChartType.ISSUES_UPDATES_2W: "BLENDER_USD_CHART_ISSUES_UPDATES_2W",
    },
    Projects.HOUDINI: {
        ChartType.UNRESOLVED_ISSUES: "HOUDINI_CHART_UNRESOLVED_ISSUES",
        ChartType.ISSUES_UPDATES_2W: "HOUDINI_CHART_ISSUES_UPDATES_2W",
    },
}

CHART_HEADER_ID = {
    Projects.MAYA_RPR: {
        ChartType.UNRESOLVED_ISSUES: "MAYA_RPR_UNRESOLVED_ISSUES_HEADER",
        ChartType.ISSUES_UPDATES_2W: "MAYA_RPR_ISSUES_UPDATES_2W_HEADER",
    },
    Projects.MAYA_USD: {
        ChartType.UNRESOLVED_ISSUES: "MAYA_USD_UNRESOLVED_ISSUES_HEADER",
        ChartType.ISSUES_UPDATES_2W: "MAYA_USD_ISSUES_UPDATES_2W_HEADER",
    },
    Projects.BLENDER_RPR: {
        ChartType.UNRESOLVED_ISSUES: "BLENDER_RPR_UNRESOLVED_ISSUES_HEADER",
        ChartType.ISSUES_UPDATES_2W: "BLENDER_RPR_ISSUES_UPDATES_2W_HEADER",
    },
    Projects.BLENDER_USD: {
        ChartType.UNRESOLVED_ISSUES: "BLENDER_USD_UNRESOLVED_ISSUES_HEADER",
        ChartType.ISSUES_UPDATES_2W: "BLENDER_USD_ISSUES_UPDATES_2W_HEADER",
    },
    Projects.HOUDINI: {
        ChartType.UNRESOLVED_ISSUES: "HOUDINI_UNRESOLVED_ISSUES_HEADER",
        ChartType.ISSUES_UPDATES_2W: "HOUDINI_ISSUES_UPDATES_2W_HEADER",
    },
}


TASK_LISTS_ID = {
    Projects.MAYA_RPR: {
        TaskType.COMPLETED: "MAYA_RPR_TASK_LIST_HEADER_COMPLETED",
        TaskType.PLANNED: "MAYA_RPR_TASK_LIST_HEADER_PLANNED",
    },
    Projects.MAYA_USD: {
        TaskType.COMPLETED: "MAYA_USD_TASK_LIST_HEADER_COMPLETED",
        TaskType.PLANNED: "MAYA_USD_TASK_LIST_HEADER_PLANNED",
    },
    Projects.BLENDER_RPR: {
        TaskType.COMPLETED: "BLENDER_RPR_TASK_LIST_HEADER_COMPLETED",
        TaskType.PLANNED: "BLENDER_RPR_TASK_LIST_HEADER_PLANNED",
    },
    Projects.BLENDER_USD: {
        TaskType.COMPLETED: "BLENDER_USD_TASK_LIST_HEADER_COMPLETED",
        TaskType.PLANNED: "BLENDER_USD_TASK_LIST_HEADER_PLANNED",
    },
    Projects.HOUDINI: {
        TaskType.COMPLETED: "HOUDINI_TASK_LIST_HEADER_COMPLETED",
        TaskType.PLANNED: "HOUDINI_TASK_LIST_HEADER_PLANNED",
    },
    Projects.HDRPR: {
        TaskType.COMPLETED: "HDRPR_TASK_LIST_HEADER_COMPLETED",
        TaskType.PLANNED: "HDRPR_TASK_LIST_HEADER_PLANNED",
    },
    Projects.RENDER_STUDIO: {
        TaskType.COMPLETED: "RENDER_STUDIO_TASK_LIST_HEADER_COMPLETED",
        TaskType.PLANNED: "RENDER_STUDIO_TASK_LIST_HEADER_PLANNED",
    },
}

ISSUES_PLOT = {
    Projects.MAYA_RPR: "MAYA_RPR_ISSUES_PLOT",
    Projects.MAYA_USD: "MAYA_USD_ISSUES_PLOT",
    Projects.BLENDER_RPR: "BLENDER_RPR_ISSUES_PLOT",
    Projects.BLENDER_USD: "BLENDER_USD_ISSUES_PLOT",
    Projects.RENDER_STUDIO: "RENDER_STUDIO_ISSUES_PLOT",
    Projects.HOUDINI: "HOUDINI_ISSUES_PLOT",
}

IDS = [
    MAIN_TASKS_LIST,
    BLOCKERS_LIST,
    WML_BUILD_LINK,
    PR_STATUS_TABLE_ID[Projects.MAYA_RPR],
    PR_STATUS_TABLE_ID[Projects.BLENDER_RPR],
    PR_STATUS_TABLE_ID[Projects.BLENDER_USD],
    PR_STATUS_TABLE_ID[Projects.HOUDINI],
    CHART_ID[Projects.MAYA_RPR][ChartType.UNRESOLVED_ISSUES],
    CHART_ID[Projects.MAYA_RPR][ChartType.ISSUES_UPDATES_2W],
    CHART_ID[Projects.MAYA_USD][ChartType.UNRESOLVED_ISSUES],
    CHART_ID[Projects.MAYA_USD][ChartType.ISSUES_UPDATES_2W],
    CHART_ID[Projects.BLENDER_RPR][ChartType.UNRESOLVED_ISSUES],
    CHART_ID[Projects.BLENDER_RPR][ChartType.ISSUES_UPDATES_2W],
    CHART_ID[Projects.BLENDER_USD][ChartType.UNRESOLVED_ISSUES],
    CHART_ID[Projects.BLENDER_USD][ChartType.ISSUES_UPDATES_2W],
    CHART_ID[Projects.HOUDINI][ChartType.UNRESOLVED_ISSUES],
    CHART_ID[Projects.HOUDINI][ChartType.ISSUES_UPDATES_2W],
    TASK_LISTS_ID[Projects.MAYA_RPR][TaskType.COMPLETED],
    TASK_LISTS_ID[Projects.MAYA_RPR][TaskType.PLANNED],
    TASK_LISTS_ID[Projects.MAYA_USD][TaskType.COMPLETED],
    TASK_LISTS_ID[Projects.MAYA_USD][TaskType.PLANNED],
    TASK_LISTS_ID[Projects.BLENDER_RPR][TaskType.COMPLETED],
    TASK_LISTS_ID[Projects.BLENDER_RPR][TaskType.PLANNED],
    TASK_LISTS_ID[Projects.BLENDER_USD][TaskType.COMPLETED],
    TASK_LISTS_ID[Projects.BLENDER_USD][TaskType.PLANNED],
    TASK_LISTS_ID[Projects.HOUDINI][TaskType.COMPLETED],
    TASK_LISTS_ID[Projects.HOUDINI][TaskType.PLANNED],
    TASK_LISTS_ID[Projects.HDRPR][TaskType.COMPLETED],
    TASK_LISTS_ID[Projects.HDRPR][TaskType.PLANNED],
    TASK_LISTS_ID[Projects.RENDER_STUDIO][TaskType.COMPLETED],
    TASK_LISTS_ID[Projects.RENDER_STUDIO][TaskType.PLANNED],
    BUGS_LINK_ID[Projects.MAYA_RPR],
    BUGS_LINK_ID[Projects.MAYA_USD],
    BUGS_LINK_ID[Projects.BLENDER_RPR],
    BUGS_LINK_ID[Projects.BLENDER_USD],
    BUGS_LINK_ID[Projects.RENDER_STUDIO],
    BUGS_LINK_ID[Projects.HOUDINI],
    BUILD_STATUS_TABLE_ROW[Projects.MAYA_RPR],
    BUILD_STATUS_TABLE_ROW[Projects.MAYA_USD],
    BUILD_STATUS_TABLE_ROW[Projects.BLENDER_RPR],
    BUILD_STATUS_TABLE_ROW[Projects.BLENDER_USD],
    BUILD_STATUS_TABLE_ROW[Projects.HOUDINI],
    BUILD_STATUS_TABLE_ROW[Projects.RENDER_STUDIO],
    BUILD_STATUS_TABLE_ROW[Projects.HDRPR],
    BUILD_STATUS_TABLE_ROW[Projects.SOLIDWORKS],
    BUILD_STATUS_TABLE_ROW[Projects.MATERIALX],
    BUILD_STATUS_TABLE_ROW[Projects.USD_VIEWER_INVENTOR],
    BUILD_STATUS_TABLE_ROW[Projects.ANARI],
    BUILD_STATUS_TABLE_ROW[Projects.BLENDER_HIP],
    CHART_HEADER_ID[Projects.MAYA_RPR][ChartType.UNRESOLVED_ISSUES],
    CHART_HEADER_ID[Projects.MAYA_RPR][ChartType.ISSUES_UPDATES_2W],
    CHART_HEADER_ID[Projects.MAYA_USD][ChartType.UNRESOLVED_ISSUES],
    CHART_HEADER_ID[Projects.MAYA_USD][ChartType.ISSUES_UPDATES_2W],
    CHART_HEADER_ID[Projects.BLENDER_RPR][ChartType.UNRESOLVED_ISSUES],
    CHART_HEADER_ID[Projects.BLENDER_RPR][ChartType.ISSUES_UPDATES_2W],
    CHART_HEADER_ID[Projects.BLENDER_USD][ChartType.UNRESOLVED_ISSUES],
    CHART_HEADER_ID[Projects.BLENDER_USD][ChartType.ISSUES_UPDATES_2W],
    CHART_HEADER_ID[Projects.HOUDINI][ChartType.UNRESOLVED_ISSUES],
    CHART_HEADER_ID[Projects.HOUDINI][ChartType.ISSUES_UPDATES_2W],
    SUMMARY_TABLE[Projects.MAYA_RPR][SummaryTableColumn.FOUND_ISSUES],
    SUMMARY_TABLE[Projects.MAYA_RPR][SummaryTableColumn.MERGED_PRS],
    SUMMARY_TABLE[Projects.MAYA_USD][SummaryTableColumn.FOUND_ISSUES],
    SUMMARY_TABLE[Projects.MAYA_USD][SummaryTableColumn.MERGED_PRS],
    SUMMARY_TABLE[Projects.BLENDER_RPR][SummaryTableColumn.FOUND_ISSUES],
    SUMMARY_TABLE[Projects.BLENDER_RPR][SummaryTableColumn.MERGED_PRS],
    SUMMARY_TABLE[Projects.BLENDER_USD][SummaryTableColumn.FOUND_ISSUES],
    SUMMARY_TABLE[Projects.BLENDER_USD][SummaryTableColumn.MERGED_PRS],
    SUMMARY_TABLE[Projects.RENDER_STUDIO][SummaryTableColumn.FOUND_ISSUES],
    SUMMARY_TABLE[Projects.RENDER_STUDIO][SummaryTableColumn.MERGED_PRS],
    SUMMARY_TABLE[Projects.HOUDINI][SummaryTableColumn.FOUND_ISSUES],
    SUMMARY_TABLE[Projects.HOUDINI][SummaryTableColumn.MERGED_PRS],
    ISSUES_PLOT[Projects.MAYA_RPR],
    ISSUES_PLOT[Projects.MAYA_USD],
    ISSUES_PLOT[Projects.BLENDER_RPR],
    ISSUES_PLOT[Projects.BLENDER_USD],
    ISSUES_PLOT[Projects.RENDER_STUDIO],
    ISSUES_PLOT[Projects.HOUDINI],
]

REPORT_PERIOD_FIELD_ID = "REPORT_PERIOD"
