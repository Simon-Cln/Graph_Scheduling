import React from 'react';
import { 
    Paper, 
    Typography, 
    Box,
    Chip,
    Divider,
    List,
    ListItem,
    ListItemText
} from '@mui/material';

interface CriticalPathDisplayProps {
    criticalPath: number[];
    tasks: {
        id: number;
        duration: number;
        early: number;
        late: number;
        margin: number;
    }[];
}

const CriticalPathDisplay: React.FC<CriticalPathDisplayProps> = ({ criticalPath, tasks }) => {
    const getTotalDuration = () => {
        return criticalPath.reduce((total, taskId) => {
            const task = tasks.find(t => t.id === taskId);
            return total + (task?.duration || 0);
        }, 0);
    };

    return (
        <Paper sx={{ p: 3, mb: 3 }}>
            <Typography variant="h6" gutterBottom>
                Critical Path Analysis
            </Typography>
            <Box sx={{ display: 'flex', gap: 2, mb: 2 }}>
                <Chip 
                    label={`Total Duration: ${getTotalDuration()} units`}
                    color="primary"
                    variant="outlined"
                />
                <Chip 
                    label={`${criticalPath.length} Tasks`}
                    color="secondary"
                    variant="outlined"
                />
            </Box>
            <Divider sx={{ my: 2 }} />
            <List>
                {criticalPath.map((taskId, index) => {
                    const task = tasks.find(t => t.id === taskId);
                    if (!task) return null;

                    return (
                        <ListItem key={taskId}>
                            <ListItemText
                                primary={`Task ${task.id}`}
                                secondary={
                                    <>
                                        <Typography component="span" variant="body2">
                                            Duration: {task.duration}
                                        </Typography>
                                        <br />
                                        <Typography component="span" variant="body2">
                                            Early Start: {task.early}
                                        </Typography>
                                        <br />
                                        <Typography component="span" variant="body2">
                                            Late Start: {task.late}
                                        </Typography>
                                        <br />
                                        <Typography component="span" variant="body2" color="error">
                                            Margin: {task.margin}
                                        </Typography>
                                    </>
                                }
                            />
                        </ListItem>
                    );
                })}
            </List>
        </Paper>
    );
};

export default CriticalPathDisplay;
