import React from 'react';
import { 
    Table, 
    TableBody, 
    TableCell, 
    TableContainer, 
    TableHead, 
    TableRow, 
    Paper, 
    Typography 
} from '@mui/material';

interface CalendarDisplayProps {
    calendar: {
        early_dates: number[];
        late_dates: number[];
        total_margins: number[];
        free_margins: number[];
    };
}

const CalendarDisplay: React.FC<CalendarDisplayProps> = ({ calendar }) => {
    if (!calendar) return null;

    return (
        <TableContainer component={Paper} sx={{ margin: 2, padding: 2 }}>
            <Typography variant="h6" sx={{ p: 2 }}>
                Calendrier et Marges
            </Typography>
            <Table size="small">
                <TableHead>
                    <TableRow>
                        <TableCell>Tâche</TableCell>
                        <TableCell align="center">Date au plus tôt</TableCell>
                        <TableCell align="center">Date au plus tard</TableCell>
                        <TableCell align="center">Marge totale</TableCell>
                        <TableCell align="center">Marge libre</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {calendar.early_dates.map((_, index) => (
                        <TableRow key={index}>
                            <TableCell>Tâche {index + 1}</TableCell>
                            <TableCell align="center">{calendar.early_dates[index]}</TableCell>
                            <TableCell align="center">{calendar.late_dates[index]}</TableCell>
                            <TableCell align="center">{calendar.total_margins[index]}</TableCell>
                            <TableCell align="center">{calendar.free_margins[index]}</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
};

export default CalendarDisplay;
