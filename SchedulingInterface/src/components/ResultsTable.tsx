import React from 'react';
import {
    Paper,
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow,
    Typography,
    Box,
    Tabs,
    Tab
} from '@mui/material';
import { GraphData, Task } from '../types/graphTypes';

interface ResultsTableProps {
    data: GraphData;
}

interface TabPanelProps {
    children?: React.ReactNode;
    index: number;
    value: number;
}

const TabPanel = (props: TabPanelProps) => {
    const { children, value, index, ...other } = props;

    return (
        <div
            role="tabpanel"
            hidden={value !== index}
            id={`tabpanel-${index}`}
            aria-labelledby={`tab-${index}`}
            {...other}
        >
            {value === index && (
                <Box sx={{ p: 3 }}>
                    {children}
                </Box>
            )}
        </div>
    );
};

const ResultsTable: React.FC<ResultsTableProps> = ({ data }) => {
    const [value, setValue] = React.useState(0);

    const handleChange = (event: React.SyntheticEvent, newValue: number) => {
        setValue(newValue);
    };

    return (
        <Paper sx={{ width: '100%', overflow: 'hidden' }}>
            <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
                <Tabs value={value} onChange={handleChange}>
                    <Tab label="Tasks" />
                    <Tab label="Calendar" />
                </Tabs>
            </Box>

            <TabPanel value={value} index={0}>
                <TableContainer>
                    <Typography variant="h6" gutterBottom>
                        Task Details
                    </Typography>
                    <Table>
                        <TableHead>
                            <TableRow>
                                <TableCell>Task ID</TableCell>
                                <TableCell>Duration</TableCell>
                                <TableCell>Dependencies</TableCell>
                                <TableCell>Early Date</TableCell>
                                <TableCell>Late Date</TableCell>
                                <TableCell>Total Margin</TableCell>
                                <TableCell>Free Margin</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {data.tasks.map((task) => (
                                <TableRow 
                                    key={task.id.toString()}
                                    sx={data.criticalPath.includes(task.id.toString()) ? { 
                                        backgroundColor: 'rgba(255, 118, 117, 0.1)' 
                                    } : {}}
                                >
                                    <TableCell>{task.id}</TableCell>
                                    <TableCell>{task.duration}</TableCell>
                                    <TableCell>{task.dependencies.join(', ')}</TableCell>
                                    <TableCell>{task.early_dates}</TableCell>
                                    <TableCell>{task.late_dates}</TableCell>
                                    <TableCell>{task.total_margins}</TableCell>
                                    <TableCell>{task.free_margins}</TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            </TabPanel>

            <TabPanel value={value} index={1}>
                <TableContainer>
                    <Typography variant="h6" gutterBottom>
                        Calendar View
                    </Typography>
                    <Table>
                        <TableHead>
                            <TableRow>
                                <TableCell>Task</TableCell>
                                <TableCell>Early Date</TableCell>
                                <TableCell>Late Date</TableCell>
                                <TableCell>Total Margin</TableCell>
                                <TableCell>Free Margin</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {data.calendar.early_dates.map((_, index) => (
                                <TableRow key={index}>
                                    <TableCell>Task {index + 1}</TableCell>
                                    <TableCell>{data.calendar.early_dates[index]}</TableCell>
                                    <TableCell>{data.calendar.late_dates[index]}</TableCell>
                                    <TableCell>{data.calendar.total_margins[index]}</TableCell>
                                    <TableCell>{data.calendar.free_margins[index]}</TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            </TabPanel>
        </Paper>
    );
};

export default ResultsTable;
